#
# Copyright (c) 2022, TU/e Robotics
# All rights reserved.
#
# Author: Rein Appeldoorn

import actionlib
import rospy
from picovoice_msgs.msg import GetIntentAction, GetIntentGoal

from hmi import AbstractHMIServer, HMIResult


class Server(AbstractHMIServer):
    def __init__(self, name: str, context_url: str, require_endpoint: bool, rate: float):
        super(Server, self).__init__(name)

        self._context_url = context_url
        self._require_endpoint = require_endpoint
        self._rate = rate

        self._intent_client = actionlib.SimpleActionClient("get_intent", GetIntentAction)
        rospy.loginfo(f"Waiting for {self._intent_client.action_client.ns} ..")
        self._intent_client.wait_for_server()

        rospy.loginfo(f"Server initialized (context_url={context_url}, require_endpoint={require_endpoint})")

    def _determine_answer(self, description, grammar, target, is_preempt_requested):
        self._intent_client.send_goal(
            GetIntentGoal(
                context_url=self._context_url,
                require_endpoint=self._require_endpoint,
                intents=[grammar],
            )
        )

        r = rospy.Rate(self._rate)
        while not rospy.is_shutdown():
            if is_preempt_requested():
                self._intent_client.cancel_all_goals()
                self._intent_client.wait_for_result()
                return None

            result = self._intent_client.get_result()
            if result is not None:
                return (
                    HMIResult(
                        semantics={kv.key: kv.value for kv in result.slots},
                        sentence=result.intent,
                    )
                    if result.is_understood
                    else None
                )

            r.sleep()

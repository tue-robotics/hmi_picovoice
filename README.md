# hmi_picovoice

Provides a hmi interface connecting to picovoice rhino speech recognition.

It depends on [`picovoice_driver`](https://github.com/reinzor/picovoice_ros) to interface with PicoVoice's backend.

## Usage with `hmi` framework

```bash
export PICOVOICE_KEY=...  # Get from https://console.picovoice.ai, and choose eg the coffeeMaker example context
rosrun picovoice_driver picovoice_driver_rhino _access_key:=$PICOVOICE_KEY __ns:=/robot/hmi
```

```bash
rosrun hmi multi_client __name:=/robot/hmi
```

```bash
rosrun actionlib_tools axclient.py /robot/hmi
```

and in `axclient.py` GUI Client specify `grammar: 'orderBeverage'` and hit SEND GOAL.
Then, say/speak out loud e.g. 'large cappucino' to your computer and if all is well, the Result field should show something like:
```yaml
talker_id: ''
sentence: "orderBeverage"
semantics: "{\"size\": \"large\", \"beverage\": \"cappuccino\"}"
```
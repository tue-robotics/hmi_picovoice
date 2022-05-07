# hmi_picovoice

[![CI](https://github.com/tue-robotics/hmi_picovoice/actions/workflows/main.yml/badge.svg)](https://github.com/tue-robotics/hmi_picovoice/actions/workflows/main.yml) [![Lint](https://github.com/tue-robotics/hmi_picovoice/actions/workflows/lint.yml/badge.svg)](https://github.com/tue-robotics/hmi_picovoice/actions/workflows/lint.yml)

Provides a hmi interface connecting to picovoice rhino speech recognition.

It depends on [`picovoice_driver`](https://github.com/reinzor/picovoice_ros) to interface with PicoVoice's backend.

## Usage with `hmi` framework

```bash
export PICOVOICE_KEY=...  # Get from https://console.picovoice.ai, and choose eg the coffeeMaker example context
rosrun picovoice_driver picovoice_driver_rhino _access_key:=$PICOVOICE_KEY __ns:=/robot/hmi
```

```bash
rosrun hmi_picovoice hmi_picovoice_node.py _context_url:=coffee_maker_linux __ns:=/robot/hmi
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

## Parameters
For `hmi_picovoice_node.py`:
- `context_url` what model to use. **TODO**: Not sure where eg. the string `coffee_maker_linux` comes from
- `require_endpoint` ["If set to False, Rhino does not require an endpoint (chunk of silence) before finishing inference"](https://picovoice.ai/docs/api/rhino-python/)

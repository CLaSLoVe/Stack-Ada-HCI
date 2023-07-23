# Stack ada HCI (stack-based adaptive human-computer interaction system) 🧑‍💻💻

Stack ada HCI is a stack-based adaptive human-computer interaction system. This repository builds an abstract architecture for human-computer interaction systems that estimates perception bias by stacking human perception states. Perception information is estimated through eye-tracking coordinates. The configuration files include `aois.ini`:

```
[AOI1]
x = 100
y = 100
width = 200
height = 200
panels = Panel1, Panel2
```

and `port.ini`:

```
[eye_tracking]
host = localhost
port = 8001
process_func = process_eye_tracking_data

[scene_parameter]
host = localhost
port = 8002
process_func = process_scene_parameter_data
```

It also includes `usr_func.py`:

```python
def process_eye_tracking_data(data):
    return ...

def process_scene_parameter_data(data):
    return ...
```

The architecture estimates the perception bias of a person by using eye-tracking coordinates and scene state data with a variable sampling rate. The architecture is precise and fast and can be configured by the user. This project is released under the MIT license. 🚀👨‍👩‍👧‍👦📝

## Getting Started 🚀

To get started with Stack ada HCI, you need to have Python installed on your machine. Clone the repository to your local machine and run the following command:

```
python test/server_send.py
```

```
python main.py
```

This will start the test script and the system, and you can then start configuring it according to your needs. 🏃‍♀️🏃‍♂️💻

## Contributing 🤝

Contributions are welcome and appreciated. Please fork the repository and create a pull request with your changes. 🙌🤗🎉

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details. 📜🔒👍
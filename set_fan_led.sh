#!/bin/bash
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led1 color fixed ff0067
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led2 color fixed ff00c6
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led1 color fixed ff2200
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led2 color fixed ff1000
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led3 color fixed e400ff

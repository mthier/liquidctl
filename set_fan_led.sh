#!/bin/bash
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led1 color fixed ff322d
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led2 color fixed ff322d
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led1 color fixed ff322d
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led2 color fixed ff322d
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led3 color fixed ff322d

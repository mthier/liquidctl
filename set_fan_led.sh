#!/bin/bash
COLOR=AF77FE
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led1 color fixed $COLOR
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led2 color fixed $COLOR
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller Kraken" set led3 color fixed $COLOR
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led1 color fixed $COLOR
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led2 color fixed $COLOR
sudo /opt/liquidctl/venv/bin/python3 -m liquidctl --match "NZXT RGB Controller F-Series" set led3 color fixed $COLOR

~~~
Tesla Wall Connector
It has an api but documentation by Tesla is non-existant.
https://teslamotorsclub.com/tmc/threads/gen3-wall-connector-api.228034/

A few things that you can use to get info:
curl -s http://172.1.1.17/api/1/vitals | jq

Jq neatens up the JSON output
apt install jq

tesla@ubuntu:~$ curl -s http://172.19.19.171/api/1/vitals | jq
{
  "contactor_closed": false,
  "vehicle_connected": false,
  "session_s": 0,
  "grid_v": 237.5,
  "grid_hz": 59.88,
  "vehicle_current_a": 0.4,
  "currentA_a": 0,
  "currentB_a": 0.4,
  "currentC_a": 0,
  "currentN_a": 0.4,
  "voltageA_v": 4.7,
  "voltageB_v": 6.9,
  "voltageC_v": 0.1,
  "relay_coil_v": 11.9,
  "pcba_temp_c": 17.4,
  "handle_temp_c": 14.7,
  "mcu_temp_c": 21.4,
  "uptime_s": 104615,
  "input_thermopile_uv": -125,
  "prox_v": 0,
  "pilot_high_v": 11.8,
  "pilot_low_v": 11.8,
  "session_energy_wh": 19582.301,
  "config_status": 5,
  "evse_state": 1,
  "current_alerts": []
____________________________________________________________________________________

I tried this too: https://pypi.org/project/tesla-wall-connector/
But all I got was: 
tesla@ubuntu123:~$ python3 teslapy.py 
energy_wh: 28460Wh

Which is basically the number from curl -s http://172.19.19.171/api/1/lifetime | jq
{
  "contactor_cycles": 3,
  "contactor_cycles_loaded": 1,
  "alert_count": 5,
  "thermal_foldbacks": 0,
  "avg_startup_temp": 0,
  "charge_starts": 3,
  "energy_wh": 28460,
  "connector_cycles": 2,
  "uptime_s": 110259,
  "charging_time_s": 10335
}


tesla@ubuntu123:~$ curl -s http://172.19.19.171/api/1/wifi_status | jq
{
  "wifi_ssid": "TmFuby1pb3Q=",
  "wifi_signal_strength": 66,
  "wifi_rssi": -57,
  "wifi_snr": 37,
  "wifi_connected": true,
  "wifi_infra_ip": "172.19.19.171",
  "internet": true,
  "wifi_mac": "98:ED:5C:B9:35:FA"
}

tesla@ubuntu:~$ curl -s http://172.1.1.17/api/1/version | jq
{
  "firmware_version": "22.33.1+g8757aaf2fb9df0",
  "part_number": "1509549-02-B",
  "serial_number": "B7S22209J02013"
}

~~~


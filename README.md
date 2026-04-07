# ETS2 & ATS2 Shared Memory in Python!
THis repo can be used to get live data from both of the games. You can use this data for live telemetry of your vehicles to create dashboards or other apps that you need!

## Disclaimer
The script will work only after you correctly install the SDKs .dll in your plugins folder, refer to https://github.com/RenCloud/scs-sdk-plugin.

## Usage
To get the various fields refer to the chart below. The SDK has two main classes **scsTrailer_s** and **scsTelemetryMap_s**.
You can use ```from_buffer_copy``` from ctypes to read the memoryMap in either the trailer or the telemetry class. 
Based on the data from the buffer you can then read various fields without needing to manually set the offsets of the fields. *(I havent personally tested all of the fields, feel free to open a issue or try to fix it yourself!)*

## Example
This example takes the data from the telemetry class and prints the trucks speed, RPM and the status of our left turn signal.
```
telemetry = scsTelemetryMap_s.from_buffer_copy(memoryMap)
# gets the speeed and the engine rpm from the truck
print(round(telemetry.truck_f.speed * 3.6)) # convert to km/h
print(round(telemetry.truck_f.engineRpm))
print(telemetry.truck_b.blinkerLeftActive)
```
Thanks to RenCloud for creating and updating the initial SDK.

## All of the fields
### scsTrailer_s

| Class | Field                        | Data Type          |
|--------------|-----------------------------|---------------------|
| con_b        | wheelSteerable              | `c_bool[16]`        |
| con_b        | wheelSimulated              | `c_bool[16]`        |
| con_b        | wheelPowered                | `c_bool[16]`        |
| con_b        | wheelLiftable               | `c_bool[16]`        |
| com_b        | wheelOnGround               | `c_bool[16]`        |
| com_b        | attached                    | `c_bool`            |
| com_ui       | wheelSubstance              | `c_uint[16]`        |
| con_ui       | wheelCount                  | `c_uint`            |
| com_f        | cargoDamage                 | `c_float`           |
| com_f        | wearChassis                 | `c_float`           |
| com_f        | wearWheels                  | `c_float`           |
| com_f        | wearBody                    | `c_float`           |
| com_f        | wheelSuspDeflection         | `c_float[16]`       |
| com_f        | wheelVelocity               | `c_float[16]`       |
| com_f        | wheelSteering               | `c_float[16]`       |
| com_f        | wheelRotation               | `c_float[16]`       |
| com_f        | wheelLift                   | `c_float[16]`       |
| com_f        | wheelLiftOffset             | `c_float[16]`       |
| con_f        | wheelRadius                 | `c_float[16]`       |
| com_fv       | linearVelocityX             | `c_float`           |
| com_fv       | linearVelocityY             | `c_float`           |
| com_fv       | linearVelocityZ             | `c_float`           |
| com_fv       | angularVelocityX            | `c_float`           |
| com_fv       | angularVelocityY            | `c_float`           |
| com_fv       | angularVelocityZ            | `c_float`           |
| com_fv       | linearAccelerationX         | `c_float`           |
| com_fv       | linearAccelerationY         | `c_float`           |
| com_fv       | linearAccelerationZ         | `c_float`           |
| com_fv       | angularAccelerationX        | `c_float`           |
| com_fv       | angularAccelerationY        | `c_float`           |
| com_fv       | angularAccelerationZ        | `c_float`           |
| con_fv       | hookPositionX               | `c_float`           |
| con_fv       | hookPositionY               | `c_float`           |
| con_fv       | hookPositionZ               | `c_float`           |
| con_fv       | wheelPositionX              | `c_float[16]`       |
| con_fv       | wheelPositionY              | `c_float[16]`       |
| con_fv       | wheelPositionZ              | `c_float[16]`       |
| con_dp       | worldX                      | `c_double`          |
| con_dp       | worldY                      | `c_double`          |
| con_dp       | worldZ                      | `c_double`          |
| con_dp       | rotationX                   | `c_double`          |
| con_dp       | rotationY                   | `c_double`          |
| con_dp       | rotationZ                   | `c_double`          |
| con_s        | id                          | `c_char[64]`        |
| con_s        | cargoAcessoryId             | `c_char[64]`        |
| con_s        | bodyType                    | `c_char[64]`        |
| con_s        | brandId                     | `c_char[64]`        |
| con_s        | brand                       | `c_char[64]`        |
| con_s        | name                        | `c_char[64]`        |
| con_s        | chainType                   | `c_char[64]`        |
| con_s        | licensePlate                | `c_char[64]`        |
| con_s        | licensePlateCountry         | `c_char[64]`        |
| con_s        | licensePlateCountryId       | `c_char[64]`        |

### scsTelemetryMap_s

| Class     | Field                          | Data Type             |
|------------------|-------------------------------|------------------------|
| -                | sdkActive                     | `c_bool`               |
| -                | placeHolder                   | `c_char[3]`            |
| -                | paused                        | `c_bool`               |
| -                | placeHolder2                  | `c_char[3]`            |
| -                | time                          | `c_ulonglong`          |
| -                | simulatedTime                 | `c_ulonglong`          |
| -                | renderTime                    | `c_ulonglong`          |
| -                | multiplayerTimeOffset         | `c_longlong`           |
| scs_values       | telemetry_plugin_revision     | `c_uint`               |
| scs_values       | version_major                 | `c_uint`               |
| scs_values       | version_minor                 | `c_uint`               |
| scs_values       | game                          | `c_uint`               |
| scs_values       | telemetry_version_game_major  | `c_uint`               |
| scs_values       | telemetry_version_game_minor  | `c_uint`               |
| common_ui        | time_abs                      | `c_uint`               |
| config_ui        | gears                         | `c_uint`               |
| config_ui        | gears_reverse                 | `c_uint`               |
| config_ui        | retarderStepCount             | `c_uint`               |
| config_ui        | truckWheelCount               | `c_uint`               |
| config_ui        | selectorCount                 | `c_uint`               |
| config_ui        | time_abs_delivery             | `c_uint`               |
| config_ui        | maxTrailerCount               | `c_uint`               |
| config_ui        | unitCount                     | `c_uint`               |
| config_ui        | plannedDistanceKm             | `c_uint`               |
| truck_ui         | shifterSlot                   | `c_uint`               |
| truck_ui         | retarderBrake                 | `c_uint`               |
| truck_ui         | lightsAuxFront                | `c_uint`               |
| truck_ui         | lightsAuxRoof                 | `c_uint`               |
| truck_ui         | truck_wheelSubstance          | `c_uint[16]`           |
| truck_ui         | hshifterPosition              | `c_uint[32]`           |
| truck_ui         | hshifterBitmask               | `c_uint[32]`           |
| gameplay_ui      | jobDeliveredDeliveryTime      | `c_uint`               |
| gameplay_ui      | jobStartingTime               | `c_uint`               |
| gameplay_ui      | jobFinishedTime               | `c_uint`               |
| common_i         | restStop                      | `c_int`                |
| truck_i          | gear                          | `c_int`                |
| truck_i          | gearDashboard                 | `c_int`                |
| truck_i          | hshifterResulting             | `c_int[32]`            |
| gameplay_i       | jobDeliveredEarnedXp          | `c_int`                |
| common_f         | scale                         | `c_float`              |
| config_f         | fuelCapacity                  | `c_float`              |
| config_f         | fuelWarningFactor             | `c_float`              |
| config_f         | adblueCapacity                | `c_float`              |
| config_f         | adblueWarningFactor           | `c_float`              |
| config_f         | airPressureWarning            | `c_float`              |
| config_f         | airPressurEmergency           | `c_float`              |
| config_f         | oilPressureWarning            | `c_float`              |
| config_f         | waterTemperatureWarning       | `c_float`              |
| config_f         | batteryVoltageWarning         | `c_float`              |
| config_f         | engineRpmMax                  | `c_float`              |
| config_f         | gearDifferential              | `c_float`              |
| config_f         | cargoMass                     | `c_float`              |
| config_f         | truckWheelRadius              | `c_float[16]`          |
| config_f         | gearRatiosForward             | `c_float[24]`          |
| config_f         | gearRatiosReverse             | `c_float[8]`           |
| config_f         | unitMass                      | `c_float`              |
| gameplay_f       | jobDeliveredCargoDamage       | `c_float`              |
| gameplay_f       | jobDeliveredDistanceKm        | `c_float`              |
| gameplay_f       | refuelAmount                  | `c_float`              |
| job_f            | cargoDamage                   | `c_float`              |
| config_b         | truckWheelSteerable           | `c_bool[16]`           |
| config_b         | truckWheelSimulated           | `c_bool[16]`           |
| config_b         | truckWheelPowered             | `c_bool[16]`           |
| config_b         | truckWheelLiftable            | `c_bool[16]`           |
| config_b         | isCargoLoaded                 | `c_bool`               |
| config_b         | specialJob                    | `c_bool`               |
| truck_b          | parkBrake                     | `c_bool`               |
| truck_b          | motorBrake                    | `c_bool`               |
| truck_b          | airPressureWarning            | `c_bool`               |
| truck_b          | airPressureEmergency          | `c_bool`               |
| truck_b          | fuelWarning                   | `c_bool`               |
| truck_b          | adblueWarning                 | `c_bool`               |
| truck_b          | oilPressureWarning            | `c_bool`               |
| truck_b          | waterTemperatureWarning       | `c_bool`               |
| truck_b          | batteryVoltageWarning         | `c_bool`               |
| truck_b          | electricEnabled               | `c_bool`               |
| truck_b          | engineEnabled                 | `c_bool`               |
| truck_b          | wipers                        | `c_bool`               |
| truck_b          | blinkerLeftActive             | `c_bool`               |
| truck_b          | blinkerRightActive            | `c_bool`               |
| truck_b          | blinkerLeftOn                 | `c_bool`               |
| truck_b          | blinkerRightOn                | `c_bool`               |
| truck_b          | lightsParking                 | `c_bool`               |
| truck_b          | lightsBeamLow                 | `c_bool`               |
| truck_b          | lightsBeamHigh                | `c_bool`               |
| truck_b          | lightsBeacon                  | `c_bool`               |
| truck_b          | lightsBrake                   | `c_bool`               |
| truck_b          | lightsReverse                 | `c_bool`               |
| truck_b          | lightsHazard                  | `c_bool`               |
| truck_b          | cruiseControl                 | `c_bool`               |
| truck_b          | truck_wheelOnGround           | `c_bool[16]`           |
| truck_b          | shifterToggle                 | `c_bool[2]`            |
| truck_b          | differentialLock              | `c_bool`               |
| truck_b          | liftAxle                      | `c_bool`               |
| truck_b          | liftAxleIndicator             | `c_bool`               |
| truck_b          | trailerLiftAxle               | `c_bool`               |
| truck_b          | trailerLiftAxleIndicator      | `c_bool`               |
| gameplay_b       | jobDeliveredAutoparkUsed      | `c_bool`               |
| gameplay_b       | jobDeliveredAutoloadUsed      | `c_bool`               |
| config_fv        | cabinPositionX                | `c_float`              |
| config_fv        | cabinPositionY                | `c_float`              |
| config_fv        | cabinPositionZ                | `c_float`              |
| config_fv        | headPositionX                 | `c_float`              |
| config_fv        | headPositionY                 | `c_float`              |
| config_fv        | headPositionZ                 | `c_float`              |
| config_fv        | truckHookPositionX            | `c_float`              |
| config_fv        | truckHookPositionY            | `c_float`              |
| config_fv        | truckHookPositionZ            | `c_float`              |
| config_fv        | truckWheelPositionX           | `c_float[16]`          |
| config_fv        | truckWheelPositionY           | `c_float[16]`          |
| config_fv        | truckWheelPositionZ           | `c_float[16]`          |
| truck_fv         | lv_accelerationX              | `c_float`              |
| truck_fv         | lv_accelerationY              | `c_float`              |
| truck_fv         | lv_accelerationZ              | `c_float`              |
| truck_fv         | av_accelerationX              | `c_float`              |
| truck_fv         | av_accelerationY              | `c_float`              |
| truck_fv         | av_accelerationZ              | `c_float`              |
| truck_fv         | accelerationX                 | `c_float`              |
| truck_fv         | accelerationY                 | `c_float`              |
| truck_fv         | accelerationZ                 | `c_float`              |
| truck_fv         | aa_accelerationX              | `c_float`              |
| truck_fv         | aa_accelerationY              | `c_float`              |
| truck_fv         | aa_accelerationZ              | `c_float`              |
| truck_fv         | cabinAVX                      | `c_float`              |
| truck_fv         | cabinAVY                      | `c_float`              |
| truck_fv         | cabinAVZ                      | `c_float`              |
| truck_fv         | cabinAAX                      | `c_float`              |
| truck_fv         | cabinAAY                      | `c_float`              |
| truck_fv         | cabinAAZ                      | `c_float`              |
| truck_fp         | cabinOffsetX                  | `c_float`              |
| truck_fp         | cabinOffsetY                  | `c_float`              |
| truck_fp         | cabinOffsetZ                  | `c_float`              |
| truck_fp         | cabinOffsetrotationX          | `c_float`              |
| truck_fp         | cabinOffsetrotationY          | `c_float`              |
| truck_fp         | cabinOffsetrotationZ          | `c_float`              |
| truck_fp         | headOffsetX                   | `c_float`              |
| truck_fp         | headOffsetY                   | `c_float`              |
| truck_fp         | headOffsetZ                   | `c_float`              |
| truck_fp         | headOffsetrotationX           | `c_float`              |
| truck_fp         | headOffsetrotationY           | `c_float`              |
| truck_fp         | headOffsetrotationZ           | `c_float`              |
| truck_dp         | coordinateX                   | `c_double`             |
| truck_dp         | coordinateY                   | `c_double`             |
| truck_dp         | coordinateZ                   | `c_double`             |
| truck_dp         | rotationX                     | `c_double`             |
| truck_dp         | rotationY                     | `c_double`             |
| truck_dp         | rotationZ                     | `c_double`             |
| config_s         | truckBrandId                  | `c_char[64]`           |
| config_s         | truckBrand                    | `c_char[64]`           |
| config_s         | truckId                       | `c_char[64]`           |
| config_s         | truckName                     | `c_char[64]`           |
| config_s         | cargoId                       | `c_char[64]`           |
| config_s         | cargo                         | `c_char[64]`           |
| config_s         | cityDstId                     | `c_char[64]`           |
| config_s         | cityDst                       | `c_char[64]`           |
| config_s         | compDstId                     | `c_char[64]`           |
| config_s         | compDst                       | `c_char[64]`           |
| config_s         | citySrcId                     | `c_char[64]`           |
| config_s         | citySrc                       | `c_char[64]`           |
| config_s         | compSrcId                     | `c_char[64]`           |
| config_s         | compSrc                       | `c_char[64]`           |
| config_s         | shifterType                   | `c_char[16]`           |
| config_s         | truckLicensePlate             | `c_char[64]`           |
| config_s         | truckLicensePlateCountryId    | `c_char[64]`           |
| config_s         | truckLicensePlateCountry      | `c_char[64]`           |
| config_s         | jobMarket                     | `c_char[32]`           |
| gameplay_s       | fineOffence                   | `c_char[32]`           |
| gameplay_s       | ferrySourceName               | `c_char[64]`           |
| gameplay_s       | ferryTargetName               | `c_char[64]`           |
| gameplay_s       | ferrySourceId                 | `c_char[64]`           |
| gameplay_s       | ferryTargetId                 | `c_char[64]`           |
| gameplay_s       | trainSourceName               | `c_char[64]`           |
| gameplay_s       | trainTargetName               | `c_char[64]`           |
| gameplay_s       | trainSourceId                 | `c_char[64]`           |
| gameplay_s       | trainTargetId                 | `c_char[64]`           |
| config_ull       | jobIncome                     | `c_ulonglong`          |
| gameplay_ll      | jobCancelledPenalty           | `c_longlong`           |
| gameplay_ll      | jobDeliveredRevenue           | `c_longlong`           |
| gameplay_ll      | fineAmount                    | `c_longlong`           |
| gameplay_ll      | tollgatePayAmount             | `c_longlong`           |
| gameplay_ll      | ferryPayAmount                | `c_longlong`           |
| gameplay_ll      | trainPayAmount                | `c_longlong`           |
| special_b        | onJob                         | `c_bool`               |
| special_b        | jobFinished                   | `c_bool`               |
| special_b        | jobCancelled                  | `c_bool`               |
| special_b        | jobDelivered                  | `c_bool`               |
| special_b        | fined                         | `c_bool`               |
| special_b        | tollgate                      | `c_bool`               |
| special_b        | ferry                         | `c_bool`               |
| special_b        | train                         | `c_bool`               |
| special_b        | refuel                        | `c_bool`               |
| special_b        | refuelPayed                   | `c_bool`               |
| substances       | substance                     | `(c_char[64])[25]`     |
| -                | trailer                       | `scsTrailer_s[10]`     |


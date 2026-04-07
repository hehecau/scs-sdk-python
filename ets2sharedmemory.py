import mmap
import ctypes

MMAP_NAME = "Local\\SCSTelemetry"
MMAP_SIZE = 32 * 1024 

import ctypes

class scsTrailer_s(ctypes.Structure):
    class con_b(ctypes.Structure):
        _fields_ = [
            ("wheelSteerable", ctypes.c_bool * 16),
            ("wheelSimulated", ctypes.c_bool * 16),
            ("wheelPowered", ctypes.c_bool * 16),
            ("wheelLiftable", ctypes.c_bool * 16),
        ]

    class com_b(ctypes.Structure):
        _fields_ = [
            ("wheelOnGround", ctypes.c_bool * 16),
            ("attached", ctypes.c_bool),
        ]

    class com_ui(ctypes.Structure):
        _fields_ = [
            ("wheelSubstance", ctypes.c_uint * 16),
        ]

    class con_ui(ctypes.Structure):
        _fields_ = [
            ("wheelCount", ctypes.c_uint),
        ]

    class com_f(ctypes.Structure):
        _fields_ = [
            ("cargoDamage", ctypes.c_float),
            ("wearChassis", ctypes.c_float),
            ("wearWheels", ctypes.c_float),
            ("wearBody", ctypes.c_float),
            ("wheelSuspDeflection", ctypes.c_float * 16),
            ("wheelVelocity", ctypes.c_float * 16),
            ("wheelSteering", ctypes.c_float * 16),
            ("wheelRotation", ctypes.c_float * 16),
            ("wheelLift", ctypes.c_float * 16),
            ("wheelLiftOffset", ctypes.c_float * 16),
        ]

    class con_f(ctypes.Structure):
        _fields_ = [
            ("wheelRadius", ctypes.c_float * 16),
        ]

    class com_fv(ctypes.Structure):
        _fields_ = [
            ("linearVelocityX", ctypes.c_float),
            ("linearVelocityY", ctypes.c_float),
            ("linearVelocityZ", ctypes.c_float),
            ("angularVelocityX", ctypes.c_float),
            ("angularVelocityY", ctypes.c_float),
            ("angularVelocityZ", ctypes.c_float),
            ("linearAccelerationX", ctypes.c_float),
            ("linearAccelerationY", ctypes.c_float),
            ("linearAccelerationZ", ctypes.c_float),
            ("angularAccelerationX", ctypes.c_float),
            ("angularAccelerationY", ctypes.c_float),
            ("angularAccelerationZ", ctypes.c_float),
        ]

    class con_fv(ctypes.Structure):
        _fields_ = [
            ("hookPositionX", ctypes.c_float),
            ("hookPositionY", ctypes.c_float),
            ("hookPositionZ", ctypes.c_float),
            ("wheelPositionX", ctypes.c_float * 16),
            ("wheelPositionY", ctypes.c_float * 16),
            ("wheelPositionZ", ctypes.c_float * 16),
        ]

    class con_dp(ctypes.Structure):
        _fields_ = [
            ("worldX", ctypes.c_double),
            ("worldY", ctypes.c_double),
            ("worldZ", ctypes.c_double),
            ("rotationX", ctypes.c_double),
            ("rotationY", ctypes.c_double),
            ("rotationZ", ctypes.c_double),
        ]

    class con_s(ctypes.Structure):
        _fields_ = [
            ("id", ctypes.c_char * 64),
            ("cargoAcessoryId", ctypes.c_char * 64),
            ("bodyType", ctypes.c_char * 64),
            ("brandId", ctypes.c_char * 64),
            ("brand", ctypes.c_char * 64),
            ("name", ctypes.c_char * 64),
            ("chainType", ctypes.c_char * 64),
            ("licensePlate", ctypes.c_char * 64),
            ("licensePlateCountry", ctypes.c_char * 64),
            ("licensePlateCountryId", ctypes.c_char * 64),
        ]

    _fields_ = [
        ("con_b", con_b),
        ("com_b", com_b),
        ("buffer_b", ctypes.c_char * 3),

        ("com_ui", com_ui),
        ("con_ui", con_ui),

        ("com_f", com_f),
        ("con_f", con_f),

        ("com_fv", com_fv),
        ("con_fv", con_fv),
        ("buffer_fv", ctypes.c_char * 4),

        ("com_dp", con_dp),

        ("con_s", con_s),
    ]

class scsTelemetryMap_s(ctypes.Structure):
    class truck_f(ctypes.Structure):
        _fields_ = [
            ("speed", ctypes.c_float),
            ("engineRpm", ctypes.c_float),
            ("userSteer", ctypes.c_float),
            ("userThrottle", ctypes.c_float),
            ("userBrake", ctypes.c_float),
            ("userClutch", ctypes.c_float),
            ("gameSteer", ctypes.c_float),
            ("gameThrottle", ctypes.c_float),
            ("gameBrake", ctypes.c_float),
            ("gameClutch", ctypes.c_float),
            ("cruiseControlSpeed", ctypes.c_float),
            ("airPressure", ctypes.c_float),
            ("brakeTemperature", ctypes.c_float),
            ("fuel", ctypes.c_float),
            ("fuelAvgConsumption", ctypes.c_float),
            ("fuelRange", ctypes.c_float),
            ("adblue", ctypes.c_float),
            ("oilPressure", ctypes.c_float),
            ("oilTemperature", ctypes.c_float),
            ("waterTemperature", ctypes.c_float),
            ("batteryVoltage", ctypes.c_float),
            ("lightsDashboard", ctypes.c_float),
            ("wearEngine", ctypes.c_float),
            ("wearTransmission", ctypes.c_float),
            ("wearCabin", ctypes.c_float),
            ("wearChassis", ctypes.c_float),
            ("wearWheels", ctypes.c_float),
            ("truckOdometer", ctypes.c_float),
            ("routeDistance", ctypes.c_float),
            ("routeTime", ctypes.c_float),
            ("speedLimit", ctypes.c_float),
            ("truck_wheelSuspDeflection", ctypes.c_float * 16),
            ("truck_wheelVelocity", ctypes.c_float * 16),
            ("truck_wheelSteering", ctypes.c_float * 16),
            ("truck_wheelRotation", ctypes.c_float * 16),
            ("truck_wheelLift", ctypes.c_float * 16),
            ("truck_wheelLiftOffset", ctypes.c_float * 16),
        ]

    class scs_values(ctypes.Structure):
        _fields_ = [
            ("telemetry_plugin_revision", ctypes.c_uint),
            ("version_major", ctypes.c_uint),
            ("version_minor", ctypes.c_uint),
            ("game", ctypes.c_uint),
            ("telemetry_version_game_major", ctypes.c_uint),
            ("telemetry_version_game_minor", ctypes.c_uint),
        ]

    class common_ui(ctypes.Structure):
        _fields_ = [
            ("time_abs", ctypes.c_uint),
        ]

    class config_ui(ctypes.Structure):
        _fields_ = [
            ("gears", ctypes.c_uint),
            ("gears_reverse", ctypes.c_uint),
            ("retarderStepCount", ctypes.c_uint),
            ("truckWheelCount", ctypes.c_uint),
            ("selectorCount", ctypes.c_uint),
            ("time_abs_delivery", ctypes.c_uint),
            ("maxTrailerCount", ctypes.c_uint),
            ("unitCount", ctypes.c_uint),
            ("plannedDistanceKm", ctypes.c_uint),
        ]

    class truck_ui(ctypes.Structure):
        _fields_ = [
            ("shifterSlot", ctypes.c_uint),
            ("retarderBrake", ctypes.c_uint),
            ("lightsAuxFront", ctypes.c_uint),
            ("lightsAuxRoof", ctypes.c_uint),
            ("truck_wheelSubstance", ctypes.c_uint * 16),
            ("hshifterPosition", ctypes.c_uint * 32),
            ("hshifterBitmask", ctypes.c_uint * 32),
        ]

    class gameplay_ui(ctypes.Structure):
        _fields_ = [
            ("jobDeliveredDeliveryTime", ctypes.c_uint),
            ("jobStartingTime", ctypes.c_uint),
            ("jobFinishedTime", ctypes.c_uint),
        ]

    class common_i(ctypes.Structure):
        _fields_ = [
            ("restStop", ctypes.c_int),
        ]

    class truck_i(ctypes.Structure):
        _fields_ = [
            ("gear", ctypes.c_int),
            ("gearDashboard", ctypes.c_int),
            ("hshifterResulting", ctypes.c_int * 32),
        ]

    class gameplay_i(ctypes.Structure):
        _fields_ = [
            ("jobDeliveredEarnedXp", ctypes.c_int),
        ]

    class common_f(ctypes.Structure):
        _fields_ = [
            ("scale", ctypes.c_float),
        ]

    class config_f(ctypes.Structure):
        _fields_ = [
            ("fuelCapacity", ctypes.c_float),
            ("fuelWarningFactor", ctypes.c_float),
            ("adblueCapacity", ctypes.c_float),
            ("adblueWarningFactor", ctypes.c_float),
            ("airPressureWarning", ctypes.c_float),
            ("airPressurEmergency", ctypes.c_float),
            ("oilPressureWarning", ctypes.c_float),
            ("waterTemperatureWarning", ctypes.c_float),
            ("batteryVoltageWarning", ctypes.c_float),
            ("engineRpmMax", ctypes.c_float),
            ("gearDifferential", ctypes.c_float),
            ("cargoMass", ctypes.c_float),
            ("truckWheelRadius", ctypes.c_float * 16),
            ("gearRatiosForward", ctypes.c_float * 24),
            ("gearRatiosReverse", ctypes.c_float * 8),
            ("unitMass", ctypes.c_float),
        ]

    class gameplay_f(ctypes.Structure):
        _fields_ = [
            ("jobDeliveredCargoDamage", ctypes.c_float),
            ("jobDeliveredDistanceKm", ctypes.c_float),
            ("refuelAmount", ctypes.c_float),
        ]

    class job_f(ctypes.Structure):
        _fields_ = [
            ("cargoDamage", ctypes.c_float),
        ]

    class config_b(ctypes.Structure):
        _fields_ = [
            ("truckWheelSteerable", ctypes.c_bool * 16),
            ("truckWheelSimulated", ctypes.c_bool * 16),
            ("truckWheelPowered", ctypes.c_bool * 16),
            ("truckWheelLiftable", ctypes.c_bool * 16),
            ("isCargoLoaded", ctypes.c_bool),
            ("specialJob", ctypes.c_bool),
        ]

    class truck_b(ctypes.Structure):
        _fields_ = [
            ("parkBrake", ctypes.c_bool),
            ("motorBrake", ctypes.c_bool),
            ("airPressureWarning", ctypes.c_bool),
            ("airPressureEmergency", ctypes.c_bool),
            ("fuelWarning", ctypes.c_bool),
            ("adblueWarning", ctypes.c_bool),
            ("oilPressureWarning", ctypes.c_bool),
            ("waterTemperatureWarning", ctypes.c_bool),
            ("batteryVoltageWarning", ctypes.c_bool),
            ("electricEnabled", ctypes.c_bool),
            ("engineEnabled", ctypes.c_bool),
            ("wipers", ctypes.c_bool),
            ("blinkerLeftActive", ctypes.c_bool),
            ("blinkerRightActive", ctypes.c_bool),
            ("blinkerLeftOn", ctypes.c_bool),
            ("blinkerRightOn", ctypes.c_bool),
            ("lightsParking", ctypes.c_bool),
            ("lightsBeamLow", ctypes.c_bool),
            ("lightsBeamHigh", ctypes.c_bool),
            ("lightsBeacon", ctypes.c_bool),
            ("lightsBrake", ctypes.c_bool),
            ("lightsReverse", ctypes.c_bool),
            ("lightsHazard", ctypes.c_bool),
            ("cruiseControl", ctypes.c_bool),
            ("truck_wheelOnGround", ctypes.c_bool * 16),
            ("shifterToggle", ctypes.c_bool * 2),
            ("differentialLock", ctypes.c_bool),
            ("liftAxle", ctypes.c_bool),
            ("liftAxleIndicator", ctypes.c_bool),
            ("trailerLiftAxle", ctypes.c_bool),
            ("trailerLiftAxleIndicator", ctypes.c_bool),
        ]

    class gameplay_b(ctypes.Structure):
        _fields_ = [
            ("jobDeliveredAutoparkUsed", ctypes.c_bool),
            ("jobDeliveredAutoloadUsed", ctypes.c_bool),
        ]

    class config_fv(ctypes.Structure):
        _fields_ = [
            ("cabinPositionX", ctypes.c_float),
            ("cabinPositionY", ctypes.c_float),
            ("cabinPositionZ", ctypes.c_float),
            ("headPositionX", ctypes.c_float),
            ("headPositionY", ctypes.c_float),
            ("headPositionZ", ctypes.c_float),
            ("truckHookPositionX", ctypes.c_float),
            ("truckHookPositionY", ctypes.c_float),
            ("truckHookPositionZ", ctypes.c_float),
            ("truckWheelPositionX", ctypes.c_float * 16),
            ("truckWheelPositionY", ctypes.c_float * 16),
            ("truckWheelPositionZ", ctypes.c_float * 16),
        ]

    class truck_fv(ctypes.Structure):
        _fields_ = [
            ("lv_accelerationX", ctypes.c_float),
            ("lv_accelerationY", ctypes.c_float),
            ("lv_accelerationZ", ctypes.c_float),
            ("av_accelerationX", ctypes.c_float),
            ("av_accelerationY", ctypes.c_float),
            ("av_accelerationZ", ctypes.c_float),
            ("accelerationX", ctypes.c_float),
            ("accelerationY", ctypes.c_float),
            ("accelerationZ", ctypes.c_float),
            ("aa_accelerationX", ctypes.c_float),
            ("aa_accelerationY", ctypes.c_float),
            ("aa_accelerationZ", ctypes.c_float),
            ("cabinAVX", ctypes.c_float),
            ("cabinAVY", ctypes.c_float),
            ("cabinAVZ", ctypes.c_float),
            ("cabinAAX", ctypes.c_float),
            ("cabinAAY", ctypes.c_float),
            ("cabinAAZ", ctypes.c_float),
        ]

    class truck_fp(ctypes.Structure):
        _fields_ = [
            ("cabinOffsetX", ctypes.c_float),
            ("cabinOffsetY", ctypes.c_float),
            ("cabinOffsetZ", ctypes.c_float),
            ("cabinOffsetrotationX", ctypes.c_float),
            ("cabinOffsetrotationY", ctypes.c_float),
            ("cabinOffsetrotationZ", ctypes.c_float),
            ("headOffsetX", ctypes.c_float),
            ("headOffsetY", ctypes.c_float),
            ("headOffsetZ", ctypes.c_float),
            ("headOffsetrotationX", ctypes.c_float),
            ("headOffsetrotationY", ctypes.c_float),
            ("headOffsetrotationZ", ctypes.c_float),
        ]

    class truck_dp(ctypes.Structure):
        _fields_ = [
            ("coordinateX", ctypes.c_double),
            ("coordinateY", ctypes.c_double),
            ("coordinateZ", ctypes.c_double),
            ("rotationX", ctypes.c_double),
            ("rotationY", ctypes.c_double),
            ("rotationZ", ctypes.c_double),
        ]

    class config_s(ctypes.Structure):
        _fields_ = [
            ("truckBrandId", ctypes.c_char * 64),
            ("truckBrand", ctypes.c_char * 64),
            ("truckId", ctypes.c_char * 64),
            ("truckName", ctypes.c_char * 64),
            ("cargoId", ctypes.c_char * 64),
            ("cargo", ctypes.c_char * 64),
            ("cityDstId", ctypes.c_char * 64),
            ("cityDst", ctypes.c_char * 64),
            ("compDstId", ctypes.c_char * 64),
            ("compDst", ctypes.c_char * 64),
            ("citySrcId", ctypes.c_char * 64),
            ("citySrc", ctypes.c_char * 64),
            ("compSrcId", ctypes.c_char * 64),
            ("compSrc", ctypes.c_char * 64),
            ("shifterType", ctypes.c_char * 16),
            ("truckLicensePlate", ctypes.c_char * 64),
            ("truckLicensePlateCountryId", ctypes.c_char * 64),
            ("truckLicensePlateCountry", ctypes.c_char * 64),
            ("jobMarket", ctypes.c_char * 32),
        ]

    class gameplay_s(ctypes.Structure):
        _fields_ = [
            ("fineOffence", ctypes.c_char * 32),
            ("ferrySourceName", ctypes.c_char * 64),
            ("ferryTargetName", ctypes.c_char * 64),
            ("ferrySourceId", ctypes.c_char * 64),
            ("ferryTargetId", ctypes.c_char * 64),
            ("trainSourceName", ctypes.c_char * 64),
            ("trainTargetName", ctypes.c_char * 64),
            ("trainSourceId", ctypes.c_char * 64),
            ("trainTargetId", ctypes.c_char * 64),
        ]

    class config_ull(ctypes.Structure):
        _fields_ = [
            ("jobIncome", ctypes.c_ulonglong),
        ]

    class gameplay_ll(ctypes.Structure):
        _fields_ = [
            ("jobCancelledPenalty", ctypes.c_longlong),
            ("jobDeliveredRevenue", ctypes.c_longlong),
            ("fineAmount", ctypes.c_longlong),
            ("tollgatePayAmount", ctypes.c_longlong),
            ("ferryPayAmount", ctypes.c_longlong),
            ("trainPayAmount", ctypes.c_longlong),
        ]

    class special_b(ctypes.Structure):
        _fields_ = [
            ("onJob", ctypes.c_bool),
            ("jobFinished", ctypes.c_bool),
            ("jobCancelled", ctypes.c_bool),
            ("jobDelivered", ctypes.c_bool),
            ("fined", ctypes.c_bool),
            ("tollgate", ctypes.c_bool),
            ("ferry", ctypes.c_bool),
            ("train", ctypes.c_bool),
            ("refuel", ctypes.c_bool),
            ("refuelPayed", ctypes.c_bool),
        ]

    class substances(ctypes.Structure):
        _fields_ = [
            ("substance", (ctypes.c_char * 64) * 25),
        ]

    # all of the structs
    _fields_ = [
        ("sdkActive", ctypes.c_bool),
        ("placeHolder", ctypes.c_char * 3),
        ("paused", ctypes.c_bool),
        ("placeHolder2", ctypes.c_char * 3),
        ("time", ctypes.c_ulonglong),
        ("simulatedTime", ctypes.c_ulonglong),
        ("renderTime", ctypes.c_ulonglong),
        ("multiplayerTimeOffset", ctypes.c_longlong),

        ("scs_values", scs_values),
        ("common_ui", common_ui),
        ("config_ui", config_ui),
        ("truck_ui", truck_ui),
        ("gameplay_ui", gameplay_ui),
        ("buffer_ui", ctypes.c_char * 48),

        ("common_i", common_i),
        ("truck_i", truck_i),
        ("gameplay_i", gameplay_i),
        ("buffer_i", ctypes.c_char * 56),

        ("common_f", common_f),
        ("config_f", config_f),
        ("truck_f", truck_f),
        ("gameplay_f", gameplay_f),
        ("job_f", job_f),
        ("buffer_f", ctypes.c_char * 28),

        ("config_b", config_b),
        ("truck_b", truck_b),
        ("gameplay_b", gameplay_b),
        ("buffer_b", ctypes.c_char * 25),

        ("config_fv", config_fv),
        ("truck_fv", truck_fv),
        ("buffer_fv", ctypes.c_char * 60),

        ("truck_fp", truck_fp),
        ("buffer_fp", ctypes.c_char * 152),

        ("truck_dp", truck_dp),
        ("buffer_dp", ctypes.c_char * 52),

        ("config_s", config_s),
        ("gameplay_s", gameplay_s),
        ("buffer_s", ctypes.c_char * 20),

        ("config_ull", config_ull),
        ("buffer_ull", ctypes.c_char * 192),

        ("gameplay_ll", gameplay_ll),
        ("buffer_ll", ctypes.c_char * 52),

        ("special_b", special_b),
        ("buffer_special", ctypes.c_char * 90),

        ("substances", substances),

        ("trailer", scsTrailer_s * 10),
    ]


memoryMap = mmap.mmap(-1, MMAP_SIZE, MMAP_NAME, access=mmap.ACCESS_READ)

# example for usage
telemetry = scsTelemetryMap_s.from_buffer_copy(memoryMap)
# gets the speeed and the engine rpm from the truck
print(round(telemetry.truck_f.speed * 3.6)) # defaultly its in m/s
print(round(telemetry.truck_f.engineRpm))
print(telemetry.truck_b.blinkerLeftActive)









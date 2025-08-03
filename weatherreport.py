

def sensorStub_rainy():
    return {
        'temperatureInC': 30,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def sensorStub_hihgprecipitation():
    return {
        'temperatureInC': 35,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 40
    }

def sensorStub_Sunny():
    return {
        'temperatureInC': 23,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 40
    }

def sensorStub_Cloudy():
    return {
        'temperatureInC': 30,
        'precipitation': 40,
        'humidity': 26,
        'windSpeedKMPH': 40
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = 'Partly Cloudy'   
        elif readings['precipitation'] >= 60:
            if readings['windSpeedKMPH'] > 50:
                weather = "Alert, Stormy with heavy rain"
            else:
                weather = 'Heavy Rain'
    return weather


def testRainy():
    weather = report(sensorStub_rainy)
    print(weather)
    assert("Stormy" in weather)

def testSunny():
    weather = report(sensorStub_Sunny)
    print(weather)
    assert("Sunny" in weather)
    
def testCloudy():
    weather = report(sensorStub_Cloudy)
    print(weather)
    assert("Cloudy" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(sensorStub_hihgprecipitation)
    print(weather)
    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert("Heavy Rain" in weather)


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    testSunny()
    testCloudy()
    #print("All is well (maybe!)");

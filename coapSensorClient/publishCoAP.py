import asyncio
from coapSensorClient.PutRequest import putReq

def coapPublishAccelerometer(obj):
    asyncio.run(putReq(obj, uri="accelerometer"))
def coapPublishAlimeter(obj):
    asyncio.run(putReq(obj, uri="alimeter"))
def coapPublishPulse(obj):
    asyncio.run(putReq(obj, uri="pulse"))
def coapPublishWeight(obj):
    asyncio.run(putReq(obj, uri="weight"))
def coapPublishWristBand(obj):
    asyncio.run(putReq(obj, uri="wristband"))
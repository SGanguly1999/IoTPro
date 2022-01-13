import logging
import asyncio
from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def putReq(object, uri=None):
 """Perform a single PUT request to localhost on the default port, URI
    "/other/block". The request is sent 2 seconds after initialization.

    The payload is bigger than 1kB, and thus sent as several blocks."""
 k=1
 while k != None:
    context = await Context.create_client_context()

    await asyncio.sleep(1 // object.sampleFreq)
    k = object.output()
    print(k)
    if(k !=None):
     request = Message(code = PUT, payload=bytes(str(k),'ascii'), uri="coap://localhost/"+uri)
     response = await context.request(request).response
     print('Result: %s\n%r'%(response.code, response.payload))

# Copyright (c) 2017 Jevgenijs Protopopovs
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from aiohttp import web

def read_file(path):
    with open(path, 'r') as fl:
        return fl.read().strip()

async def get_battery_state():
    path = '/sys/class/power_supply/%s'
    state = {
        'battery': {
            'capacity': int(read_file(path % 'BAT0/capacity')),
            'capacity_level': read_file(path % 'BAT0/capacity_level'),
            'charge_full': int(read_file(path % 'BAT0/charge_full')),
            'charge_now': int(read_file(path % 'BAT0/charge_now')),
            'status': read_file(path % 'BAT0/status'),
            'technology': read_file(path % 'BAT0/technology'),
            'manufacturer': read_file(path % 'BAT0/manufacturer'),
            'model': read_file(path % 'BAT0/model_name')
        },
        'ac': {
            'online': int(read_file(path % 'AC/online')) == 1
        }
    }
    return state

async def battery_get(request):
    return web.json_response(await get_battery_state())

def route_init(app):
    app.router.add_get('/', battery_get)

if __name__ == '__main__':
    app = web.Application()
    route_init(app)
    web.run_app(app, host=sys.argv[1], port=int(sys.argv[2]))
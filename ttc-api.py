import requests


class TTCApi:
    def __init__(self, lang="ka"):
        if lang == "ka":
            self.BASE_URL = "http://transfer.ttc.com.ge:8080/otp/routers/ttc"
        elif lang == "en":
            self.BASE_URL = "http://transferen.ttc.com.ge:18080/otp/routers/ttc"
        else:
            raise ValueError("Unsupported language")

    def send_request(self, url, params=None):
        headers = {"accept": "application/json"}
        url = f"{self.BASE_URL}{url}"
        req = requests.get(url, params=params, headers=headers)
        return req

    def search_stop(self, name: str):
        params = {"name": name}
        res = self.send_request("/stops", params)
        return res.json()

    def all_routes(self):
        res = self.send_request("/routes")
        return res.json()["Route"]

    def bus_routes(self):
        params = {"type": 3}
        res = self.send_request("/routes", params)
        return res.json()["Route"]

    def all_stops(self):
        res = self.send_request("/index/stops")
        return res.json()

    def stop_info(self, stop_id: str):
        res = self.send_request(f"/index/stops/{stop_id}")
        return res.json()

    def stop_routes(self, stop_id: str):
        res = self.send_request(f"/index/stops/{stop_id}/routes")
        return res.json()

    def stop_arrival_times(self, stop_id: str):
        params = {"stopId": stop_id}
        res = self.send_request("/stopArrivalTimes", params)
        return res.json()

    def bus_route_info(self, route_number: str, forward: bool):
        params = {"routeNumber": route_number, "type": "bus", "forward": int(forward)}
        res = self.send_request("/routeInfo", params)
        return res.json()

    def bus_live_locations(self, route_number: str, forward: bool):
        params = {"routeNumber": route_number, "type": "bus", "forward": int(forward)}
        res = self.send_request("/buses", params)
        return res.json()

    def route_stops(self, route_number: str, forward: bool):
        params = {"routeNumber": route_number, "forward": int(forward)}
        res = self.send_request("/routeStops", params)
        return res.json()

    def scheme_stops(self, route_number: str, forward: bool):
        params = {"routeNumber": route_number, "forward": int(forward)}
        res = self.send_request("/schemeStops", params)
        return res.json()

    def route_schedule(self, route_number: str, forward: bool):
        params = {"routeNumber": route_number, "type": 3, "forward": int(forward)}
        res = self.send_request("/routeSchedule", params)
        return res.json()

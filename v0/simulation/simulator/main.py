import time


class Simulator:
    def __init__(self, frame_rate):
        self.frames = []
        self.frame_rate = frame_rate

    def time_between_frames(self):
        current_frame = self.frames[len(self.frames) - 1]
        previous_frame = self.frames[len(self.frames) - 2]

        return current_frame["timestamp"] - previous_frame["timestamp"]

    def generate_frame(self, new_time):
        new_id = len(self.frames) + 1
        frame = {
            "version": "0.0.0",
            "frame_id": new_id,
            "timestamp": new_time,
            "sim_data": {
                "ambience": {
                    "temperature": {
                        "unit": "F",
                        "value": 97.6
                    },
                },
                "dut": { # THis should be ephemeris, not a DUT....DUT is per test.
                    "position": {
                        "x": 0,
                        "y": 0,
                        "z": 0,
                    },
                    "temperature": {
                        "unit": "F",
                        "value": 82.1
                    },
                }
            }
        }

        return frame

    def simulator(self):
        while(True):
            time.sleep(self.frame_rate)

            new_time = f"{time.time():.9f}: "
            frame = self.generate_frame(new_time=new_time)

            # if len(self.frames) > 0:
            #     print(self.time_between_frames())

            print(frame)

            self.frames.append(frame)

def main():
    sim = Simulator(frame_rate = .001)
    sim.simulator()


if __name__ == "__main__":
    main()
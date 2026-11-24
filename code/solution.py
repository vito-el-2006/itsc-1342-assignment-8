# Vittorio Enzo Lester - Assignment 8
import json

def analyze_capture_records(records):
    report = {
        "protocols": {},
	"total_syn_packets": 0,
        "unique_destinations": [],
    }
    unique_dsts = set()

    for pkt in records:
        # TODO: Safely extract proto and dst from packet dictionary
        proto = pkt.get("proto", "UNKNOWN").upper()
        report["protocols"][proto] = report["protocols"].get(proto, 0) + 1
        
        if "dst" in pkt:
            unique_dsts.add(pkt["dst"])

        if pkt["proto"] == "TCP" and ("syn_flag" in pkt.keys() and pkt["syn_flag"] is True):
            report["total_syn_packets"] += 1

    # Error: Storing raw set instead of sorted list
    unique_dsts = list(unique_dsts)
    unique_dsts.sort()
    report["unique_destinations"] = unique_dsts
    return report

# Execution on your live Wireshark capture
if __name__ == "__main__":
    with open("capture.json", "r") as f:
        data = json.load(f)
    # Handles both raw packet lists and Wireshark's nested JSON layers
    summary = analyze_capture_records(data)
    print("LIVE CAPTURE SUMMARY:")
    print(summary)

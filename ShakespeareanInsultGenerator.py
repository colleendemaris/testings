import random

def main():
    column_one = ("artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered",
        "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning",
        "fobbing", "froward", "frothy", "gleeking", "goatish", "gorbellied", "impertinent", "infectious",
        "jarring", "loggerhead", "lumpish", "mammering", "mangled", "mewling", "paunchy", "pribbling",
        "puking", "puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", "spleeny", "spongy",
        "surly", "tottering", "unmuzzled", "vain", "venomed", "villanous", "warped", "wayward", "weedy", "yeasty")
    column_two = ("base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed",
        "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted",
        "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen",
        "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated",
        "idle-headed", "ill-breeding", "ill-nurtered", "knotty-pated", "milk-livered", "motley-minded", "onion-eyed",
        "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed",
        "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted",
        "unchin-snouted", "weather-bitten")
    column_three = ("apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bug-bear", "bum-bailey", "canker-blossom",
        "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench", "flirt-gill",
        "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger",
        "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp",
        "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet",
        "varlot", "vassal", "whey-face", "wagtail")

    enter = input("")

    while enter != "q":
        insult(column_one, column_two, column_three)
        enter = input("")


def insult(column_one, column_two, column_three):
    one = random.randint(0, 49)
    two = random.randint(0, 49)
    three = random.randint(0, 49)

    print("Thou", column_one[one], column_two[two], column_three[three], end="")
    print("!")

main()
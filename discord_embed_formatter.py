from common.schemas import MAX_DISCORD_EMBED
import logging


def format_embed_output(final_str:str) -> str:
    logging.info("embedded content length is: " + str(len(final_str)))
    if len(final_str) >= MAX_DISCORD_EMBED:
        warn_msg = "\nNote: Final output has been truncated due to exceeding limit 1024"
        final_str = final_str[:(MAX_DISCORD_EMBED-len(warn_msg))] + warn_msg
    return final_str

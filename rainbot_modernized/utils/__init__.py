"""
Utility functions and helpers for rainbot
"""

from .helpers import (
    apply_vars,
    SafeString,
    SafeFormat,
    update_nested_config,
    remove_nested_config,
    status_embed,
    format_duration,
    format_timestamp,
    truncate_text,
    get_user_avatar,
    create_embed,
    safe_send,
    parse_time,
    clean_content,
    get_member_status,
    format_permissions,
    chunk_list,
    get_relative_time,
    confirm_action
)
from .errors import (
    RainBotError,
    PermissionError,
    ConfigurationError,
    ModerationError,
    DatabaseError,
    ValidationError,
    AutoModError,
    SetupError
)
from .decorators import (
    require_permission,
    has_permissions,
    get_user_permission_level
)
from .converters import (
    EmojiOrUnicode,
    MemberOrID,
    MemberOrUser,
    Duration
)
from .paginator import (
    Paginator,
    EmbedPaginator,
    ListPaginator,
    FieldPaginator,
    paginate_text
)

__all__ = [
    # Helpers
    "format_duration",
    "format_timestamp",
    "truncate_text",
    "get_user_avatar",
    "create_embed",
    "safe_send",
    # Errors
    "RainBotError",
    "PermissionError",
    "ConfigurationError",
    "ModerationError",
    # Decorators
    "require_permission",
    "cooldown",
    "guild_only",
    "owner_only",
    # Converters
    "MemberOrUser",
    "Duration",
    "BooleanConverter",
    # Paginator
    "Paginator",
    "EmbedPaginator",
]

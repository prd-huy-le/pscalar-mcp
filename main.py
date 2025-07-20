
# MCP server scaffolded from OpenAPI YAML
import os
import requests
from mcp.server.fastmcp import FastMCP

API_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")
API_KEY = os.environ.get("API_KEY")

mcp = FastMCP("My API MCP Server")

def _auth_headers():
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers

# Schema: List schemas
@mcp.tool()
def list_schemas(search: str = None, page: int = None, per_page: int = None, workspaces: str = None) -> dict:
    """List schemas the user has access to"""
    url = f"{API_URL}/api/v1/schema/"
    params = {}
    if search: params["search"] = search
    if page: params["page"] = page
    if per_page: params["per_page"] = per_page
    if workspaces: params["workspaces"] = workspaces
    resp = requests.get(url, params=params, headers=_auth_headers())
    return resp.json()

# Schema: Create schema
@mcp.tool()
def create_schema(name: str, description: str = None, scope: int = None, json_content: dict = None, workspace: int = None) -> dict:
    """Create a new schema. json_content should be a JSON object (dict)."""
    url = f"{API_URL}/api/v1/schema/"
    payload = {"name": name}
    if description: payload["description"] = description
    if scope: payload["scope"] = scope
    if json_content: payload["json_content"] = json_content
    if workspace: payload["workspace"] = workspace
    resp = requests.post(url, json=payload, headers=_auth_headers())
    return resp.json()

# Schema: Retrieve schema by ID
@mcp.tool()
def get_schema_by_id(id: int) -> dict:
    """Retrieve a schema by its ID"""
    url = f"{API_URL}/api/v1/schema/{id}/"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# Schema: Update schema (PUT)
@mcp.tool()
def update_schema(id: int, name: str, description: str = None, scope: int = None, json_content: dict = None, workspace: int = None) -> dict:
    """Update a schema (full update). json_content should be a JSON object (dict)."""
    url = f"{API_URL}/api/v1/schema/{id}/"
    payload = {"name": name}
    if description: payload["description"] = description
    if scope: payload["scope"] = scope
    if json_content: payload["json_content"] = json_content
    if workspace: payload["workspace"] = workspace
    resp = requests.put(url, json=payload, headers=_auth_headers())
    return resp.json()

# Schema: Partial update (PATCH)
@mcp.tool()
def patch_schema(id: int, name: str = None, description: str = None, scope: int = None, json_content: dict = None, workspace: int = None) -> dict:
    """Partially update a schema. json_content should be a JSON object (dict)."""
    url = f"{API_URL}/api/v1/schema/{id}/"
    payload = {}
    if name: payload["name"] = name
    if description: payload["description"] = description
    if scope: payload["scope"] = scope
    if json_content: payload["json_content"] = json_content
    if workspace: payload["workspace"] = workspace
    resp = requests.patch(url, json=payload, headers=_auth_headers())
    return resp.json()

# Schema: Retrieve by slug
@mcp.tool()
def get_schema_by_slug(slug: str) -> dict:
    """Retrieve a schema by its slug"""
    url = f"{API_URL}/api/v1/schema/slug/{slug}/"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# Draft Postman Collection: Create
@mcp.tool()
def create_draft_postman_collection(content: str) -> dict:
    """Create a new draft postman collection"""
    url = f"{API_URL}/api/v1/schema/draft-postman-collection/"
    payload = {"content": content}
    resp = requests.post(url, json=payload, headers=_auth_headers())
    return resp.json()

# Draft Postman Collection: List
@mcp.tool()
def list_draft_postman_collections() -> dict:
    """List all draft postman collections created by the current user"""
    url = f"{API_URL}/api/v1/schema/draft-postman-collection/"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# Draft Postman Collection: Retrieve by ID
@mcp.tool()
def get_draft_postman_collection_by_id(id: int) -> dict:
    """Retrieve a draft postman collection by ID"""
    url = f"{API_URL}/api/v1/schema/draft-postman-collection/{id}"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# User: Search users
@mcp.tool()
def search_users(search_q: str = None, exclude_ids: str = None) -> dict:
    """Search users"""
    url = f"{API_URL}/api/v1/user/users/search/"
    params = {}
    if search_q: params["search_q"] = search_q
    if exclude_ids: params["exclude_ids"] = exclude_ids
    resp = requests.get(url, params=params, headers=_auth_headers())
    return resp.json()

# User: Create user
@mcp.tool()
def create_user(email: str, full_name: str, avatar_url: str = None, system_role: int = None, status: int = None) -> dict:
    """Create a user"""
    url = f"{API_URL}/api/v1/user/users/"
    payload = {"email": email, "full_name": full_name}
    if avatar_url: payload["avatar_url"] = avatar_url
    if system_role: payload["system_role"] = system_role
    if status: payload["status"] = status
    resp = requests.post(url, json=payload, headers=_auth_headers())
    return resp.json()

# Workspace: List workspaces
@mcp.tool()
def list_workspaces() -> dict:
    """List workspaces the current user is a member of"""
    url = f"{API_URL}/api/v1/user/workspaces"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# Workspace: Create workspace
@mcp.tool()
def create_workspace(name: str, description: str = None, hosts: str = None, members: str = None) -> dict:
    """Create a workspace"""
    url = f"{API_URL}/api/v1/user/workspaces"
    payload = {"name": name}
    if description: payload["description"] = description
    if hosts: payload["hosts"] = hosts
    if members: payload["members"] = members
    resp = requests.post(url, json=payload, headers=_auth_headers())
    return resp.json()

# Workspace: Retrieve workspace by ID
@mcp.tool()
def get_workspace_by_id(id: int) -> dict:
    """Retrieve a workspace by its ID"""
    url = f"{API_URL}/api/v1/user/workspaces/{id}"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# Workspace: List all workspaces (simple)
@mcp.tool()
def list_simple_workspaces() -> dict:
    """List all workspaces (simple)"""
    url = f"{API_URL}/api/v1/user/workspaces/simple"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

# Workspace: Retrieve workspace with members
@mcp.tool()
def get_workspace_with_members(id: int) -> dict:
    """Retrieve a workspace by its ID (with members)"""
    url = f"{API_URL}/api/v1/user/workspaces/{id}"
    resp = requests.get(url, headers=_auth_headers())
    return resp.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")

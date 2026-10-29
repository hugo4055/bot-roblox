-- VoidBot NPC — coloque este código em um Script dentro de ServerScriptService.
-- Em Workspace, crie um rig R6/R15 chamado "VoidBotNPC".
-- O rig precisa conter Humanoid, HumanoidRootPart e Head.
-- Use apenas em experiências que você criou ou tem permissão para editar.

local Players = game:GetService("Players")
local PathfindingService = game:GetService("PathfindingService")
local Chat = game:GetService("Chat")

local npc = workspace:WaitForChild("VoidBotNPC")
local humanoid = npc:WaitForChild("Humanoid")
local root = npc:WaitForChild("HumanoidRootPart")
local head = npc:WaitForChild("Head")

local FOLLOW_DISTANCE = 45
local STOP_DISTANCE = 7
local UPDATE_SECONDS = 2

local function say(message)
    pcall(function()
        Chat:Chat(head, message, Enum.ChatColor.Blue)
    end)
end

local function nearestPlayer()
    local selected, selectedDistance = nil, FOLLOW_DISTANCE
    for _, player in ipairs(Players:GetPlayers()) do
        local character = player.Character
        local targetRoot = character and character:FindFirstChild("HumanoidRootPart")
        local targetHumanoid = character and character:FindFirstChildOfClass("Humanoid")
        if targetRoot and targetHumanoid and targetHumanoid.Health > 0 then
            local distance = (targetRoot.Position - root.Position).Magnitude
            if distance < selectedDistance then
                selected, selectedDistance = player, distance
            end
        end
    end
    return selected, selectedDistance
end

local function walkTo(destination)
    local path = PathfindingService:CreatePath({
        AgentRadius = 2, AgentHeight = 5, AgentCanJump = true,
        AgentCanClimb = true, WaypointSpacing = 4,
    })
    local ok = pcall(function()
        path:ComputeAsync(root.Position, destination)
    end)
    if not ok or path.Status ~= Enum.PathStatus.Success then
        humanoid:MoveTo(destination)
        return
    end
    for _, waypoint in ipairs(path:GetWaypoints()) do
        if humanoid.Health <= 0 then return end
        if waypoint.Action == Enum.PathWaypointAction.Jump then
            humanoid.Jump = true
        end
        humanoid:MoveTo(waypoint.Position)
        local reached = humanoid.MoveToFinished:Wait()
        if not reached then break end
    end
end

local prompt = head:FindFirstChildOfClass("ProximityPrompt")
if not prompt then
    prompt = Instance.new("ProximityPrompt")
    prompt.ActionText = "Conversar"
    prompt.ObjectText = "VoidBot"
    prompt.HoldDuration = 0
    prompt.MaxActivationDistance = 10
    prompt.Parent = head
end

prompt.Triggered:Connect(function(player)
    local replies = {
        "Oi, " .. player.DisplayName .. "! Posso te acompanhar?",
        "Vamos explorar o mapa juntos!",
        "Me mostre para onde você quer ir!",
    }
    say(replies[math.random(1, #replies)])
end)

say("Olá! Chegue perto e interaja para conversar.")
while humanoid.Health > 0 do
    local player, distance = nearestPlayer()
    if player and player.Character then
        local targetRoot = player.Character:FindFirstChild("HumanoidRootPart")
        if targetRoot and distance > STOP_DISTANCE then
            walkTo(targetRoot.Position)
        elseif targetRoot then
            humanoid:MoveTo(root.Position)
        end
    end
    task.wait(UPDATE_SECONDS)
end

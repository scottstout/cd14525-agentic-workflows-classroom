
Source: Udacity Agents Course

```mermaid

flowchart TD
  Start[Start] --> StrategicAgent[Stratigic Aid Coordinator];
    StrategicAgent --> InventoryAgent;
    StrategicAgent -->  WeatherAgent
    StrategicAgent --> RoadAgent
  subgraph Parallel Information Gathering
    InventoryAgent;
    WeatherAgent
    RoadAgent
   end
   InventoryAgent --> StrategicAgent
   WeatherAgent --> StrategicAgent
   RoadAgent --> StrategicAgent

  InventoryAgent --> Placeholder-for-result-flow;
  StrategicAgent --> DispatchDecision{Ready to Dispatch?};
  DispatchDecision -- Yes --> DispatchAgent[Dispatch Agent Executes];
  DispatchDecision -- No --> Replan[StrategicAgent: Replan or Wait];
  DispatchAgent --> Dispatch
  Dispatch --> Confirm[StrategicAgent: Confirm Delivery];
  Confirm --> End[End]
;
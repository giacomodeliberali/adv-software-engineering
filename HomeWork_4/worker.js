const { Client, Variables, logger } = require('camunda-external-task-client-js');

// configuration for the Client:
//  - 'baseUrl': url to the Process Engine
//  - 'logger': utility to automatically log important events
const config = { baseUrl: 'http://localhost:8080/engine-rest', use: logger, maxTasks: 1 };

// create a Client instance with custom configuration
const client = new Client(config);

// subscribe to the topic: 'MenuTask'
client.subscribe('MenuTask', async ({ task, taskService }) => {

  // Business Logic
  const processVariables = new Variables();

  processVariables.set("fish", "non_available");
  processVariables.set("rice", "non_available");

  if (Math.random() <= 0.4) {
    console.log("[MenuTask] Fish available");
    processVariables.set("fish", "available");
  }

  if (Math.random() <= 0.6) {
    console.log("[MenuTask] Rice available");
    processVariables.set("rice", "available");
  }

  // Callback - Complete
  console.log("[MenuTask] Complete");
  await taskService.complete(task, processVariables, null);
});

// subscribe to the topic: 'BillTask'
client.subscribe('BillTask', async ({ task, taskService }) => {

  // Business Logic
  const processVariables = new Variables();

  const riceTaken = Number(task.variables.get("riceTaken") || 0);
  const fishTaken = Number(task.variables.get("fishTaken") || 0);
  const saladTaken = Number(task.variables.get("saladTaken") || 0);

  processVariables.set("riceTaken", riceTaken);
  processVariables.set("fishTaken", fishTaken);
  processVariables.set("saladTaken", saladTaken);

  console.log("[BillTask] riceTaken = " + riceTaken);
  console.log("[BillTask] fishTaken = " + fishTaken);
  console.log("[BillTask] saladTaken = " + saladTaken);

  const riceCost = 3.0;
  const fishCost = 5.0;
  const saladCost = 2.0;

  const total = riceCost * riceTaken + fishCost * fishTaken + saladCost * saladTaken;


  console.log("[BillTask] total = " + total);

  processVariables.set("total", total);

  // Callback - Complete
  console.log("[BillTask] Complete");
  await taskService.complete(task, processVariables, null);
});


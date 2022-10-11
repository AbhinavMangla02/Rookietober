const Task = require('../modules/tasks');
const asyncWrapper = require('../middleware/async');
const { createCustomError } = require('../errors/custom-error');
const getAllTasks = asyncWrapper(async (req, res) => {
  
    const tasks = await Task.find({});
    res.status(200).json({ tasks });
 
  }); 
const createTask = asyncWrapper(async (req, res) => {
    // res.send('create task')
    
    const task = await Task.create(req.body);
    res.status(201).json({ task });
});
const getTask =asyncWrapper(async (req, res,next) => {
    // res.send('get single task')
    
        const { id: taskID } = req.params;
        const task = await Task.findOne({ _id: taskID });
    if (!task) {
        return next(createCustomError(`No task with the ID: ${taskID}`,404));
        
    }
        res.status(200).json({task});
    

})
const deleteTask =asyncWrapper(async (req, res) => {
    const { id: taskID } = req.params;
    const task = await Task.findOneAndDelete({ _id: taskID });
    if (!task) {
         return next(createCustomError(`No task with the ID: ${taskID}`, 404));

    }
    res.status(200).json({ task });
});
const updateTask =asyncWrapper(async (req, res) => { 
    
        const { id: taskID } = req.params;
        const task = await Task.findOneAndUpdate({ _id: taskID }, req.body, {
            new:true,runValidators:true
        });
            if (!task) {
        return next(createCustomError(`No task with the ID: ${taskID}`, 404));

            }
            res.status(200).json({ task });
        // return res.status(200).json({ id: taskID, body: req.body });
        
   

});
module.exports = {
    getAllTasks,createTask,getTask,updateTask,deleteTask
}
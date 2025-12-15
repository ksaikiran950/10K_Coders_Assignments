const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

window.onload = loadTasks;


addBtn.addEventListener("click", () => {
    if (taskInput.value.trim() === "") {
        alert("please enter a task !");
        return;
    }
    addTask(taskInput.value);
    taskInput.value = "";
});

function addTask(taskText){
    let li = document.createElement("li");
    li.innerHTML = `
    <span class="task">${taskText}</span>
    <button class="delete-btn">Delete</button>
    `;

    li.querySelector(".task").addEventListener("click", () => {
        li.classList.toggle("completed");
        saveTasks();
    });

    li.querySelector(".delete-btn").addEventListener("click", () => {
        li.remove();
        saveTasks();
    });

    taskList.appendChild(li);
    saveTasks();
}

function saveTasks(){
    localStorage.setItem("tasks",taskList.innerHTML);

}

function loadTasks(){
    taskList.innerHTML = localStorage.getItem("tasks") || "";


    document.querySelectorAll("#taskList li").forEach(li =>{
        li.querySelector(".task").addEventListener("click", () => {
            li.classList.toggle("completed");
            saveTasks();
        });

        li.querySelector(".delete-btn").addEventListener("click", () => {
            li.remove();
            saveTasks();
        });
    });
}
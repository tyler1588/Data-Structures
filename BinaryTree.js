class Node {
    constructor(value){
        this.left = null;
        this.right = null;
        this.value = value;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }
    insert(value){
        const newNode = new Node(value);
        if (this.root === null){
            this.root = newNode;
            return
        }
      
        let currentNode = this.root;
        while (true){
            if (value < currentNode.value){
                if (currentNode.left === null){
                    currentNode.left = newNode;
                    return
                }
                currentNode = currentNode.left;
            }
            if (value > currentNode.value){
                if (currentNode.right === null){
                    currentNode.right = newNode;
                    return
                }
                currentNode = currentNode.right;
            }
        }
    }
    lookup(value){
        if (!this.root){
            return console.log("Tree is empty")
        }

        let currentNode = this.root;
        while (true){
            if (value === currentNode.value){
                return console.log(currentNode)
            }
            else if (value < currentNode.value && currentNode.left != null){
                currentNode = currentNode.left
            }
            else if (value > currentNode.value && currentNode.right != null){
                currentNode = currentNode.right
            }
            else {
                return console.log("Node not in tree")
            }
        }
    }

    remove(value){
        if (!this.root){
            return false;
        }

        let currentNode = this.root;
        let parentNode = null;
        while (currentNode){
            if (value < currentNode.value){
                parentNode = currentNode;
                currentNode = currentNode.left;
            } else if (value > currentNode.value){
                parentNode = currentNode;
                currentNode = currentNode.right;
            } else if (currentNode.value === value){
                if (currentNode.right === null){
                    parentNode = currentNode;
                    currentNode = currentNode.left;
                } else if (currentNode.left === null) {

                } else {

                }
            }
        }

    }
}


const tree = new BinarySearchTree();

tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
tree.lookup(4);
// console.log(JSON.stringify(traverse(tree.root)));

//     9
//  4    20
// 1 6 15 170

function traverse(node){
    const tree = {value: node.value};
    tree.left = node.left === null ? null :
    traverse(node.left);
    tree.right = node.right === null ? null :
    traverse(node.right);
    return tree;
}
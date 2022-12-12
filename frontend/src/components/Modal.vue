<script>
export default {
  props: {
    show: Boolean
  }
};
</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <p>저장이 완료되었습니다.</p>
          </div>
          <div class="modal-body">
            <div class="modal-buttons" @click="$emit('moveHistory')">
              History 확인하기
            </div>
            <div class="modal-buttons" @click="$emit('close')">
              닫기
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-buttons {
  width: 150px;
  border: 1px solid #001a41;
  border-radius: 0.25rem;
  display: inline-block;
  text-align: center;
  align-items: center;
}

.modal-buttons:hover {
  background-color: #001a41;
  color: #f8f9fa;
  border-color: #001a41;
  cursor: pointer;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 500px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header {
  margin-top: 0;
}

.modal-header p {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

.modal-body {
  width: fit-content;
  margin: auto;
}

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>

import styled from "styled-components";

export const Layers = styled.div`
  display: grid;
  gap: ${(props) => props.gutter ?? "1rem"};
`;

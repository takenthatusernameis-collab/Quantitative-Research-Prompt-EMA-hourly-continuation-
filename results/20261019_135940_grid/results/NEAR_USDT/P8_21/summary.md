# EMA Hourly Continuation — NEAR/USDT P8_21

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1694 |
| net_profit_factor | 0.4467 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.9350 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -11.0438 |
| sortino_ratio | -6.3769 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 10.7885 |
| net_avg_loss | -19.0982 |
| avg_hold_time_bars | 2.7769 |
| exposure | 0.2138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

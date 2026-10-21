# EMA Hourly Continuation — RENDER/USDT P34_50

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.7824 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0636 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.1431 |
| sortino_ratio | -0.2528 |
| max_drawdown | 0.2384 |
| cagr | -0.1095 |
| net_avg_win | 75.9695 |
| net_avg_loss | -104.0323 |
| avg_hold_time_bars | 4.9901 |
| exposure | 0.0535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

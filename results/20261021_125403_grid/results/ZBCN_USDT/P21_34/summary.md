# EMA Hourly Continuation — ZBCN/USDT P21_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.9072 |
| net_win_rate | 0.5354 |
| gross_profit_factor | 1.1429 |
| gross_win_rate | 0.5354 |
| sharpe_ratio | -0.3964 |
| sortino_ratio | -0.0814 |
| max_drawdown | 0.1483 |
| cagr | -0.0387 |
| net_avg_win | 85.6626 |
| net_avg_loss | -108.7893 |
| avg_hold_time_bars | 5.7374 |
| exposure | 0.0526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

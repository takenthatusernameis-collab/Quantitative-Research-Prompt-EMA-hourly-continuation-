# EMA Hourly Continuation — ZBCN/USDT P12_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.9569 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1141 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -0.2611 |
| sortino_ratio | -0.0906 |
| max_drawdown | 0.2070 |
| cagr | -0.0498 |
| net_avg_win | 87.4159 |
| net_avg_loss | -102.9848 |
| avg_hold_time_bars | 16.8926 |
| exposure | 0.4439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

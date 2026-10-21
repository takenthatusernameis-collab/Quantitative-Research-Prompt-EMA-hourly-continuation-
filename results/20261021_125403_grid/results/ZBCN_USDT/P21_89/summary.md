# EMA Hourly Continuation — ZBCN/USDT P21_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.9350 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.1046 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -0.4069 |
| sortino_ratio | -0.1320 |
| max_drawdown | 0.2467 |
| cagr | -0.0655 |
| net_avg_win | 84.5818 |
| net_avg_loss | -100.8519 |
| avg_hold_time_bars | 11.8592 |
| exposure | 0.2727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

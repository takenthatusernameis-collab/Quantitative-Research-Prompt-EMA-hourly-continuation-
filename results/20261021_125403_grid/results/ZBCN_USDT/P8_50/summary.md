# EMA Hourly Continuation — ZBCN/USDT P8_50

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.9300 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.1014 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.5703 |
| sortino_ratio | -0.2236 |
| max_drawdown | 0.3668 |
| cagr | -0.1068 |
| net_avg_win | 84.6262 |
| net_avg_loss | -100.7512 |
| avg_hold_time_bars | 10.5970 |
| exposure | 0.3564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

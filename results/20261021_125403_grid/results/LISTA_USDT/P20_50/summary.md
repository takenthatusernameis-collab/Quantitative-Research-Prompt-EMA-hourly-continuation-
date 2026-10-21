# EMA Hourly Continuation — LISTA/USDT P20_50

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6174 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.7971 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -3.6264 |
| sortino_ratio | -1.2269 |
| max_drawdown | 0.7318 |
| cagr | -0.4310 |
| net_avg_win | 50.2513 |
| net_avg_loss | -65.2814 |
| avg_hold_time_bars | 8.2348 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

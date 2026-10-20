# EMA Hourly Continuation — BICO/USDT P20_100

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -3.9819 |
| sortino_ratio | -1.4150 |
| max_drawdown | 0.8281 |
| cagr | -0.4867 |
| net_avg_win | 46.3720 |
| net_avg_loss | -61.4180 |
| avg_hold_time_bars | 15.6447 |
| exposure | 0.4523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

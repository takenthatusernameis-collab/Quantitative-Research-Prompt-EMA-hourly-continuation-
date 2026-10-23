# EMA Hourly Continuation — GTC/USDT P26_100

**Symbol:** GTC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.8488 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -4.5684 |
| sortino_ratio | -1.6239 |
| max_drawdown | 0.8620 |
| cagr | -0.5359 |
| net_avg_win | 41.2049 |
| net_avg_loss | -56.9638 |
| avg_hold_time_bars | 12.4261 |
| exposure | 0.3592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

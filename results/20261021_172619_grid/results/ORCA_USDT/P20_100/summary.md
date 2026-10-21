# EMA Hourly Continuation — ORCA/USDT P20_100

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9950 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.6329 |
| sortino_ratio | -0.5087 |
| max_drawdown | 0.4881 |
| cagr | -0.2112 |
| net_avg_win | 68.8255 |
| net_avg_loss | -87.9752 |
| avg_hold_time_bars | 20.2411 |
| exposure | 0.4389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

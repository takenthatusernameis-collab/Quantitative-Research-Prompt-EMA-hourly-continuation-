# EMA Hourly Continuation — AUCTION/USDT P50_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6087 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -3.7344 |
| sortino_ratio | -1.1070 |
| max_drawdown | 0.7490 |
| cagr | -0.4107 |
| net_avg_win | 55.8912 |
| net_avg_loss | -78.7555 |
| avg_hold_time_bars | 8.9257 |
| exposure | 0.1794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — COTI/USDT P8_100

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.9721 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1447 |
| gross_win_rate | 0.5359 |
| sharpe_ratio | -0.1290 |
| sortino_ratio | -0.0423 |
| max_drawdown | 0.2428 |
| cagr | -0.0283 |
| net_avg_win | 87.8003 |
| net_avg_loss | -104.3031 |
| avg_hold_time_bars | 27.3650 |
| exposure | 0.6406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

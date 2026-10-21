# EMA Hourly Continuation — REQ/USDT P8_20

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.5017 |
| net_win_rate | 0.4096 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4096 |
| sharpe_ratio | -7.2087 |
| sortino_ratio | -2.6727 |
| max_drawdown | 0.9575 |
| cagr | -0.7156 |
| net_avg_win | 35.4347 |
| net_avg_loss | -49.0126 |
| avg_hold_time_bars | 5.6039 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

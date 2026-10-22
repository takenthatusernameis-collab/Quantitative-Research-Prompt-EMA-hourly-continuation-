# EMA Hourly Continuation — TNSR/USDT P89_200

**Symbol:** TNSR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8049 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9947 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1490 |
| sortino_ratio | -0.2786 |
| max_drawdown | 0.3062 |
| cagr | -0.1212 |
| net_avg_win | 79.6591 |
| net_avg_loss | -98.9714 |
| avg_hold_time_bars | 17.5208 |
| exposure | 0.2284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

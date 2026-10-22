# EMA Hourly Continuation — SKY/USDT P8_200

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.6890 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.5208 |
| sortino_ratio | -0.7549 |
| max_drawdown | 0.6361 |
| cagr | -0.2995 |
| net_avg_win | 65.1297 |
| net_avg_loss | -87.5664 |
| avg_hold_time_bars | 36.9672 |
| exposure | 0.7544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

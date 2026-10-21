# EMA Hourly Continuation — ZEC/USDT P55_200

**Symbol:** ZEC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8930 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0569 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -0.5137 |
| sortino_ratio | -0.1203 |
| max_drawdown | 0.2043 |
| cagr | -0.0565 |
| net_avg_win | 82.8381 |
| net_avg_loss | -98.5182 |
| avg_hold_time_bars | 27.9699 |
| exposure | 0.3382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

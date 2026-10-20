# EMA Hourly Continuation — LQTY/USDT P89_144

**Symbol:** LQTY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5288 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8837 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -4.5983 |
| sortino_ratio | -1.4869 |
| max_drawdown | 0.8341 |
| cagr | -0.5087 |
| net_avg_win | 39.3083 |
| net_avg_loss | -61.0027 |
| avg_hold_time_bars | 5.1591 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

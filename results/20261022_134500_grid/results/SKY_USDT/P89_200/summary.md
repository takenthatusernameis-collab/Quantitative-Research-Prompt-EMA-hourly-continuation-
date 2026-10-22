# EMA Hourly Continuation — SKY/USDT P89_200

**Symbol:** SKY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6490 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.8462 |
| sortino_ratio | -0.8110 |
| max_drawdown | 0.6356 |
| cagr | -0.3189 |
| net_avg_win | 61.7523 |
| net_avg_loss | -92.3182 |
| avg_hold_time_bars | 10.0453 |
| exposure | 0.1854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

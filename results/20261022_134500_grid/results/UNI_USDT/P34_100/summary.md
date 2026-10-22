# EMA Hourly Continuation — UNI/USDT P34_100

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5957 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9499 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -4.0404 |
| sortino_ratio | -1.4269 |
| max_drawdown | 0.8282 |
| cagr | -0.5004 |
| net_avg_win | 39.5955 |
| net_avg_loss | -62.2115 |
| avg_hold_time_bars | 9.2520 |
| exposure | 0.2670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

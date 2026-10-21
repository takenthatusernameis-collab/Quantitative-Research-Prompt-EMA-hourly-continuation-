# EMA Hourly Continuation — LQTY/USDT P21_55

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.7400 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -2.2195 |
| sortino_ratio | -0.7591 |
| max_drawdown | 0.6017 |
| cagr | -0.2937 |
| net_avg_win | 58.5180 |
| net_avg_loss | -77.9846 |
| avg_hold_time_bars | 9.6329 |
| exposure | 0.2493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

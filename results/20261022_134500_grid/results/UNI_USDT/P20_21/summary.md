# EMA Hourly Continuation — UNI/USDT P20_21

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.1336 |
| net_win_rate | 0.2785 |
| gross_profit_factor | 0.6024 |
| gross_win_rate | 0.3441 |
| sharpe_ratio | -18.3305 |
| sortino_ratio | -9.7245 |
| max_drawdown | 1.0000 |
| cagr | -0.9959 |
| net_avg_win | 4.6024 |
| net_avg_loss | -13.2970 |
| avg_hold_time_bars | 1.4904 |
| exposure | 0.0815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

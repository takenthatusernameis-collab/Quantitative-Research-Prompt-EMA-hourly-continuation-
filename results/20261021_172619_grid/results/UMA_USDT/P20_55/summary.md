# EMA Hourly Continuation — UMA/USDT P20_55

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6816 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9415 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -3.0860 |
| sortino_ratio | -1.0754 |
| max_drawdown | 0.7196 |
| cagr | -0.3902 |
| net_avg_win | 52.8590 |
| net_avg_loss | -72.9912 |
| avg_hold_time_bars | 9.1145 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

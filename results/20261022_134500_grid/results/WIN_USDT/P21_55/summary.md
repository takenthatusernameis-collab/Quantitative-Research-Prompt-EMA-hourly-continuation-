# EMA Hourly Continuation — WIN/USDT P21_55

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.3658 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.8194 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -9.7620 |
| sortino_ratio | -4.1294 |
| max_drawdown | 0.9954 |
| cagr | -0.8812 |
| net_avg_win | 16.2632 |
| net_avg_loss | -29.2787 |
| avg_hold_time_bars | 5.3296 |
| exposure | 0.2154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

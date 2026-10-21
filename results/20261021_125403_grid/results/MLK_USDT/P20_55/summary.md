# EMA Hourly Continuation — MLK/USDT P20_55

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.4465 |
| net_win_rate | 0.3831 |
| gross_profit_factor | 0.6531 |
| gross_win_rate | 0.3853 |
| sharpe_ratio | -5.3203 |
| sortino_ratio | -1.5946 |
| max_drawdown | 0.8513 |
| cagr | -0.5241 |
| net_avg_win | 39.7014 |
| net_avg_loss | -55.2069 |
| avg_hold_time_bars | 9.9131 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

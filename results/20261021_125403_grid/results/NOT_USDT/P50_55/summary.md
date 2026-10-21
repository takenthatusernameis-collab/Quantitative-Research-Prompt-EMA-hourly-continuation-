# EMA Hourly Continuation — NOT/USDT P50_55

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 1.0068 |
| net_win_rate | 0.5789 |
| gross_profit_factor | 1.3611 |
| gross_win_rate | 0.5789 |
| sharpe_ratio | 0.0479 |
| sortino_ratio | 0.0062 |
| max_drawdown | 0.0957 |
| cagr | 0.0011 |
| net_avg_win | 90.7688 |
| net_avg_loss | -123.9589 |
| avg_hold_time_bars | 6.2632 |
| exposure | 0.0224 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

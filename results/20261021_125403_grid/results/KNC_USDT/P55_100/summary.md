# EMA Hourly Continuation — KNC/USDT P55_100

**Symbol:** KNC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6156 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -3.3833 |
| sortino_ratio | -1.0097 |
| max_drawdown | 0.7145 |
| cagr | -0.3707 |
| net_avg_win | 53.1913 |
| net_avg_loss | -78.7919 |
| avg_hold_time_bars | 7.3641 |
| exposure | 0.1453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

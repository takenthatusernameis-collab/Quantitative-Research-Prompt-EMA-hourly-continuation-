# EMA Hourly Continuation — CFG/USDT P34_100

**Symbol:** CFG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.5999 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -4.1810 |
| sortino_ratio | -1.5655 |
| max_drawdown | 0.8588 |
| cagr | -0.5273 |
| net_avg_win | 38.3974 |
| net_avg_loss | -55.8994 |
| avg_hold_time_bars | 8.1465 |
| exposure | 0.2629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

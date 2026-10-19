# EMA Hourly Continuation — TWT/USDT P8_20

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1796 |
| net_profit_factor | 0.2980 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.8013 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -14.7610 |
| sortino_ratio | -8.9087 |
| max_drawdown | 1.0000 |
| cagr | -0.9900 |
| net_avg_win | 5.8391 |
| net_avg_loss | -13.3255 |
| avg_hold_time_bars | 2.7622 |
| exposure | 0.2255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

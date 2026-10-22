# EMA Hourly Continuation — TWT/USDT P12_21

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.2539 |
| net_win_rate | 0.3751 |
| gross_profit_factor | 0.7999 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -15.6218 |
| sortino_ratio | -8.9784 |
| max_drawdown | 1.0000 |
| cagr | -0.9913 |
| net_avg_win | 5.6800 |
| net_avg_loss | -13.4291 |
| avg_hold_time_bars | 2.2981 |
| exposure | 0.1668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

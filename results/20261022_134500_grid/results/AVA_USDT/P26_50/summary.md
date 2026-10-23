# EMA Hourly Continuation — AVA/USDT P26_50

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.3874 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8124 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -7.8513 |
| sortino_ratio | -3.3714 |
| max_drawdown | 0.9865 |
| cagr | -0.8149 |
| net_avg_win | 14.9434 |
| net_avg_loss | -31.2971 |
| avg_hold_time_bars | 3.6788 |
| exposure | 0.1557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

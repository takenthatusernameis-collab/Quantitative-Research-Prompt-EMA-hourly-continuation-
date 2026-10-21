# EMA Hourly Continuation — WLD/USDT P21_50

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8043 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -1.3783 |
| sortino_ratio | -0.4070 |
| max_drawdown | 0.3994 |
| cagr | -0.1714 |
| net_avg_win | 72.6113 |
| net_avg_loss | -91.1385 |
| avg_hold_time_bars | 9.2736 |
| exposure | 0.1787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

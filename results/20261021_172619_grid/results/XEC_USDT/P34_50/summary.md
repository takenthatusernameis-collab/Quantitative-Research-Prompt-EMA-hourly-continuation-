# EMA Hourly Continuation — XEC/USDT P34_50

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6114 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -3.5302 |
| sortino_ratio | -1.0260 |
| max_drawdown | 0.7270 |
| cagr | -0.3756 |
| net_avg_win | 56.0901 |
| net_avg_loss | -83.2040 |
| avg_hold_time_bars | 5.4878 |
| exposure | 0.1018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

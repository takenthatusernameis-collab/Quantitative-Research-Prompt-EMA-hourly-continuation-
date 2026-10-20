# EMA Hourly Continuation — YGG/USDT P34_100

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6484 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9702 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -3.8133 |
| sortino_ratio | -1.3790 |
| max_drawdown | 0.8214 |
| cagr | -0.4782 |
| net_avg_win | 47.6577 |
| net_avg_loss | -66.6607 |
| avg_hold_time_bars | 9.7149 |
| exposure | 0.2884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CFX/USDT P34_55

**Symbol:** CFX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.5723 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.7949 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -2.8727 |
| sortino_ratio | -0.6981 |
| max_drawdown | 0.5643 |
| cagr | -0.2739 |
| net_avg_win | 56.8528 |
| net_avg_loss | -80.7168 |
| avg_hold_time_bars | 6.5759 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

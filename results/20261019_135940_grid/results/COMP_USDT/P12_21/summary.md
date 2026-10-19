# EMA Hourly Continuation — COMP/USDT P12_21

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1569 |
| net_profit_factor | 0.1712 |
| net_win_rate | 0.3792 |
| gross_profit_factor | 0.5559 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -15.2212 |
| sortino_ratio | -8.6690 |
| max_drawdown | 1.0000 |
| cagr | -0.9886 |
| net_avg_win | 3.4726 |
| net_avg_loss | -12.3882 |
| avg_hold_time_bars | 2.4946 |
| exposure | 0.1779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

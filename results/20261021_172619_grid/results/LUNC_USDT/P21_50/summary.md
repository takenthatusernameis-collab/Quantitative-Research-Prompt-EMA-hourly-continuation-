# EMA Hourly Continuation — LUNC/USDT P21_50

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5709 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.7785 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -3.6572 |
| sortino_ratio | -1.1060 |
| max_drawdown | 0.7283 |
| cagr | -0.3984 |
| net_avg_win | 48.2043 |
| net_avg_loss | -66.6719 |
| avg_hold_time_bars | 6.9690 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

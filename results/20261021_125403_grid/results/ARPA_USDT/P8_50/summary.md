# EMA Hourly Continuation — ARPA/USDT P8_50

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.7276 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -3.4752 |
| sortino_ratio | -1.4177 |
| max_drawdown | 0.8163 |
| cagr | -0.4769 |
| net_avg_win | 54.7124 |
| net_avg_loss | -69.3701 |
| avg_hold_time_bars | 11.2784 |
| exposure | 0.4180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

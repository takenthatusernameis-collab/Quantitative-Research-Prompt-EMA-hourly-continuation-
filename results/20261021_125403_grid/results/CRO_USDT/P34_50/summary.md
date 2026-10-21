# EMA Hourly Continuation — CRO/USDT P34_50

**Symbol:** CRO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0015 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -2.0385 |
| sortino_ratio | -0.4314 |
| max_drawdown | 0.4121 |
| cagr | -0.1793 |
| net_avg_win | 61.0503 |
| net_avg_loss | -98.7500 |
| avg_hold_time_bars | 6.4306 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — FLOW/USDT P34_50

**Symbol:** FLOW/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9716 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.3636 |
| sortino_ratio | -0.5951 |
| max_drawdown | 0.5101 |
| cagr | -0.2384 |
| net_avg_win | 62.4745 |
| net_avg_loss | -91.6435 |
| avg_hold_time_bars | 4.7760 |
| exposure | 0.0669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

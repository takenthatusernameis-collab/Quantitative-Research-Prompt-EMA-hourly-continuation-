# EMA Hourly Continuation — TWT/USDT P21_50

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7408 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1154 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -2.0005 |
| sortino_ratio | -0.6726 |
| max_drawdown | 0.5967 |
| cagr | -0.2637 |
| net_avg_win | 53.2232 |
| net_avg_loss | -82.1104 |
| avg_hold_time_bars | 7.0148 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

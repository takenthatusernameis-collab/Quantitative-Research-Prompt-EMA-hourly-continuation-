# EMA Hourly Continuation — AURORA/USDT P21_34

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.4117 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.6875 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -5.1528 |
| sortino_ratio | -1.3572 |
| max_drawdown | 0.8066 |
| cagr | -0.4733 |
| net_avg_win | 41.4729 |
| net_avg_loss | -68.0027 |
| avg_hold_time_bars | 7.2537 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

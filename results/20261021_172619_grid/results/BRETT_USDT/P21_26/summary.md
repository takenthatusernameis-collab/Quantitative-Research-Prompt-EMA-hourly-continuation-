# EMA Hourly Continuation — BRETT/USDT P21_26

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.8354 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0666 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -0.7298 |
| sortino_ratio | -0.1345 |
| max_drawdown | 0.1907 |
| cagr | -0.0607 |
| net_avg_win | 87.6216 |
| net_avg_loss | -111.8781 |
| avg_hold_time_bars | 5.0839 |
| exposure | 0.0379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

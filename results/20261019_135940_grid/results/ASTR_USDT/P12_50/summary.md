# EMA Hourly Continuation — ASTR/USDT P12_50

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 1.0612 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -5.4471 |
| sortino_ratio | -2.3665 |
| max_drawdown | 0.9445 |
| cagr | -0.6811 |
| net_avg_win | 31.9269 |
| net_avg_loss | -49.3324 |
| avg_hold_time_bars | 8.9497 |
| exposure | 0.3864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

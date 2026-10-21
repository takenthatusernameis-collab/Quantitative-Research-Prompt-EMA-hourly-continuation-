# EMA Hourly Continuation — THETA/USDT P100_200

**Symbol:** THETA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.7404 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.4387 |
| sortino_ratio | -0.3325 |
| max_drawdown | 0.3575 |
| cagr | -0.1420 |
| net_avg_win | 71.1141 |
| net_avg_loss | -92.4402 |
| avg_hold_time_bars | 12.0996 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

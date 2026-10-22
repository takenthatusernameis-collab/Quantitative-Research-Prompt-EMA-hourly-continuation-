# EMA Hourly Continuation — PUFFER/USDT P100_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.7025 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -1.7120 |
| sortino_ratio | -0.3810 |
| max_drawdown | 0.3154 |
| cagr | -0.1605 |
| net_avg_win | 76.3362 |
| net_avg_loss | -94.3133 |
| avg_hold_time_bars | 14.1768 |
| exposure | 0.1588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

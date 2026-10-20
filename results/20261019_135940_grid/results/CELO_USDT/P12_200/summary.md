# EMA Hourly Continuation — CELO/USDT P12_200

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7460 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0383 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.6928 |
| sortino_ratio | -0.4547 |
| max_drawdown | 0.4526 |
| cagr | -0.1945 |
| net_avg_win | 67.4929 |
| net_avg_loss | -91.9792 |
| avg_hold_time_bars | 45.9945 |
| exposure | 0.7555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

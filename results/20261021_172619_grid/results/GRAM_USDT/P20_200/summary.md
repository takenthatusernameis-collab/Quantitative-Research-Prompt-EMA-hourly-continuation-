# EMA Hourly Continuation — GRAM/USDT P20_200

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.7166 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.7837 |
| sortino_ratio | -0.4335 |
| max_drawdown | 0.4370 |
| cagr | -0.1808 |
| net_avg_win | 71.6650 |
| net_avg_loss | -91.4585 |
| avg_hold_time_bars | 46.0928 |
| exposure | 0.6097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

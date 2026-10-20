# EMA Hourly Continuation — ROSE/USDT P34_200

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8701 |
| net_win_rate | 0.5403 |
| gross_profit_factor | 1.1491 |
| gross_win_rate | 0.5403 |
| sharpe_ratio | -0.7123 |
| sortino_ratio | -0.1839 |
| max_drawdown | 0.2896 |
| cagr | -0.0874 |
| net_avg_win | 75.9020 |
| net_avg_loss | -102.5302 |
| avg_hold_time_bars | 36.4836 |
| exposure | 0.5555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

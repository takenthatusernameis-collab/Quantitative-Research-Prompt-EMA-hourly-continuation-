# EMA Hourly Continuation — ALPINE/USDT P12_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9590 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -1.4996 |
| sortino_ratio | -0.3228 |
| max_drawdown | 0.3536 |
| cagr | -0.1405 |
| net_avg_win | 69.4070 |
| net_avg_loss | -91.7238 |
| avg_hold_time_bars | 77.8798 |
| exposure | 0.8248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

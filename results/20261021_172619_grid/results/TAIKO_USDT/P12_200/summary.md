# EMA Hourly Continuation — TAIKO/USDT P12_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8861 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0599 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -0.6136 |
| sortino_ratio | -0.1503 |
| max_drawdown | 0.2484 |
| cagr | -0.0693 |
| net_avg_win | 86.0242 |
| net_avg_loss | -103.6488 |
| avg_hold_time_bars | 56.2836 |
| exposure | 0.7435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

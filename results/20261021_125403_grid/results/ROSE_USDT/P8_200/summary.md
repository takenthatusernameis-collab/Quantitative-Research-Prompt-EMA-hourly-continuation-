# EMA Hourly Continuation — ROSE/USDT P8_200

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.9153 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -0.3943 |
| sortino_ratio | -0.0853 |
| max_drawdown | 0.2159 |
| cagr | -0.0414 |
| net_avg_win | 93.0290 |
| net_avg_loss | -107.1270 |
| avg_hold_time_bars | 80.9254 |
| exposure | 0.8387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

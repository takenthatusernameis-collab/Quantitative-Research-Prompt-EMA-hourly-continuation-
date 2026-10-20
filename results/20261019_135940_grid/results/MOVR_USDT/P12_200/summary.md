# EMA Hourly Continuation — MOVR/USDT P12_200

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5471 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.6316 |
| sortino_ratio | -1.0229 |
| max_drawdown | 0.7427 |
| cagr | -0.3988 |
| net_avg_win | 47.3580 |
| net_avg_loss | -68.6539 |
| avg_hold_time_bars | 39.2236 |
| exposure | 0.7417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

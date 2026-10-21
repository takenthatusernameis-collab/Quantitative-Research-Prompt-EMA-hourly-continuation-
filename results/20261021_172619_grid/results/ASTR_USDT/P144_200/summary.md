# EMA Hourly Continuation — ASTR/USDT P144_200

**Symbol:** ASTR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.5663 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -2.7586 |
| sortino_ratio | -0.6326 |
| max_drawdown | 0.5224 |
| cagr | -0.2508 |
| net_avg_win | 56.7704 |
| net_avg_loss | -85.8233 |
| avg_hold_time_bars | 8.8140 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

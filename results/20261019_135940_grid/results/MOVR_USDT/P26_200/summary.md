# EMA Hourly Continuation — MOVR/USDT P26_200

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -2.5673 |
| sortino_ratio | -0.7331 |
| max_drawdown | 0.6131 |
| cagr | -0.2963 |
| net_avg_win | 56.3300 |
| net_avg_loss | -78.6713 |
| avg_hold_time_bars | 29.5938 |
| exposure | 0.5596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

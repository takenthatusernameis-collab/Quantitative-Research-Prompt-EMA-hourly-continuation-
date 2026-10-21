# EMA Hourly Continuation — DEEP/USDT P21_100

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.9257 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0780 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -0.4517 |
| sortino_ratio | -0.1278 |
| max_drawdown | 0.2437 |
| cagr | -0.0619 |
| net_avg_win | 92.9238 |
| net_avg_loss | -109.1450 |
| avg_hold_time_bars | 24.4727 |
| exposure | 0.4309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

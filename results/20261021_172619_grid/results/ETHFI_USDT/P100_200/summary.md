# EMA Hourly Continuation — ETHFI/USDT P100_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.9614 |
| net_win_rate | 0.5387 |
| gross_profit_factor | 1.1585 |
| gross_win_rate | 0.5387 |
| sharpe_ratio | -0.1616 |
| sortino_ratio | -0.0385 |
| max_drawdown | 0.1328 |
| cagr | -0.0220 |
| net_avg_win | 92.4303 |
| net_avg_loss | -112.2968 |
| avg_hold_time_bars | 12.5314 |
| exposure | 0.1544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

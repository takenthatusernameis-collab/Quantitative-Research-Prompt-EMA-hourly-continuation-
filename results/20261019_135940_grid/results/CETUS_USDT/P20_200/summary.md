# EMA Hourly Continuation — CETUS/USDT P20_200

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.8858 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1297 |
| gross_win_rate | 0.5314 |
| sharpe_ratio | -0.6601 |
| sortino_ratio | -0.1629 |
| max_drawdown | 0.3160 |
| cagr | -0.0773 |
| net_avg_win | 89.0297 |
| net_avg_loss | -112.4543 |
| avg_hold_time_bars | 50.9967 |
| exposure | 0.6992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

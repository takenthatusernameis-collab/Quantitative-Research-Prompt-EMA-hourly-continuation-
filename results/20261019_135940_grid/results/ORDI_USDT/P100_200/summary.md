# EMA Hourly Continuation — ORDI/USDT P100_200

**Symbol:** ORDI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.5325 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.7863 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -3.6325 |
| sortino_ratio | -1.0317 |
| max_drawdown | 0.7224 |
| cagr | -0.3931 |
| net_avg_win | 43.7686 |
| net_avg_loss | -67.0511 |
| avg_hold_time_bars | 8.2971 |
| exposure | 0.1561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

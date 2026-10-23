# EMA Hourly Continuation — BOME/USDT P12_21

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1462 |
| net_profit_factor | 0.4058 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -11.2479 |
| sortino_ratio | -6.0450 |
| max_drawdown | 0.9996 |
| cagr | -0.9545 |
| net_avg_win | 11.1366 |
| net_avg_loss | -19.8144 |
| avg_hold_time_bars | 2.0999 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TAIKO/USDT P50_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -2.4496 |
| sortino_ratio | -0.6714 |
| max_drawdown | 0.5326 |
| cagr | -0.2636 |
| net_avg_win | 54.1908 |
| net_avg_loss | -77.8164 |
| avg_hold_time_bars | 9.1351 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HBAR/USDT P50_55

**Symbol:** HBAR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 77 |
| net_profit_factor | 0.8117 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1921 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | -0.5517 |
| sortino_ratio | -0.0703 |
| max_drawdown | 0.1409 |
| cagr | -0.0315 |
| net_avg_win | 79.3164 |
| net_avg_loss | -117.2576 |
| avg_hold_time_bars | 5.1169 |
| exposure | 0.0179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

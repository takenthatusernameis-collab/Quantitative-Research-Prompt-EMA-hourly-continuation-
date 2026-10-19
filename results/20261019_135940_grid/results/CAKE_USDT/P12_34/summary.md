# EMA Hourly Continuation — CAKE/USDT P12_34

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1211 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 1.0667 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -9.9394 |
| sortino_ratio | -4.8681 |
| max_drawdown | 0.9981 |
| cagr | -0.9166 |
| net_avg_win | 15.0692 |
| net_avg_loss | -26.6900 |
| avg_hold_time_bars | 4.6912 |
| exposure | 0.2582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

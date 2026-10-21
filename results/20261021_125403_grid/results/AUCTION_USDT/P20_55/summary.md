# EMA Hourly Continuation — AUCTION/USDT P20_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5950 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8456 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -4.3739 |
| sortino_ratio | -1.5337 |
| max_drawdown | 0.8428 |
| cagr | -0.5112 |
| net_avg_win | 43.8357 |
| net_avg_loss | -61.9518 |
| avg_hold_time_bars | 9.2463 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

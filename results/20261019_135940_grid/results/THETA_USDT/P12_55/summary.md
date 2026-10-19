# EMA Hourly Continuation — THETA/USDT P12_55

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.5667 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -6.2456 |
| sortino_ratio | -2.6856 |
| max_drawdown | 0.9650 |
| cagr | -0.7297 |
| net_avg_win | 29.4858 |
| net_avg_loss | -43.3060 |
| avg_hold_time_bars | 8.9234 |
| exposure | 0.3813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

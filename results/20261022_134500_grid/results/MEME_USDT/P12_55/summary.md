# EMA Hourly Continuation — MEME/USDT P12_55

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -5.2615 |
| sortino_ratio | -2.3231 |
| max_drawdown | 0.9415 |
| cagr | -0.6702 |
| net_avg_win | 31.3367 |
| net_avg_loss | -45.5626 |
| avg_hold_time_bars | 9.0508 |
| exposure | 0.4048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LUNA/USDT P20_144

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.5548 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.9056 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -5.1104 |
| sortino_ratio | -1.8157 |
| max_drawdown | 0.8942 |
| cagr | -0.5902 |
| net_avg_win | 38.2642 |
| net_avg_loss | -56.6961 |
| avg_hold_time_bars | 16.2016 |
| exposure | 0.4750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MEME/USDT P21_55

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.6950 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.2250 |
| sortino_ratio | -1.1147 |
| max_drawdown | 0.7561 |
| cagr | -0.4002 |
| net_avg_win | 60.1312 |
| net_avg_loss | -75.4955 |
| avg_hold_time_bars | 7.0663 |
| exposure | 0.1889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

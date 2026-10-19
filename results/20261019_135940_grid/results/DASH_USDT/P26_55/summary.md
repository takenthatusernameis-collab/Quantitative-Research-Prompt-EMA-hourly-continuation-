# EMA Hourly Continuation — DASH/USDT P26_55

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.3862 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.9400 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -7.7846 |
| sortino_ratio | -3.3490 |
| max_drawdown | 0.9857 |
| cagr | -0.8153 |
| net_avg_win | 14.7284 |
| net_avg_loss | -30.9379 |
| avg_hold_time_bars | 4.3298 |
| exposure | 0.1850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

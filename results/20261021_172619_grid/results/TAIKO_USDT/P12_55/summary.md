# EMA Hourly Continuation — TAIKO/USDT P12_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.8480 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.1028 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -1.4062 |
| sortino_ratio | -0.5077 |
| max_drawdown | 0.5369 |
| cagr | -0.2107 |
| net_avg_win | 76.9305 |
| net_avg_loss | -100.0108 |
| avg_hold_time_bars | 11.9378 |
| exposure | 0.3412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

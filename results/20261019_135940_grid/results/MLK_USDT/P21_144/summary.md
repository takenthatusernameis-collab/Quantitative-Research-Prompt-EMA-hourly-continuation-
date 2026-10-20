# EMA Hourly Continuation — MLK/USDT P21_144

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.3616 |
| net_win_rate | 0.3266 |
| gross_profit_factor | 0.5895 |
| gross_win_rate | 0.3291 |
| sharpe_ratio | -9.7706 |
| sortino_ratio | -3.8663 |
| max_drawdown | 0.9921 |
| cagr | -0.8523 |
| net_avg_win | 21.8667 |
| net_avg_loss | -29.3196 |
| avg_hold_time_bars | 13.4727 |
| exposure | 0.4798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

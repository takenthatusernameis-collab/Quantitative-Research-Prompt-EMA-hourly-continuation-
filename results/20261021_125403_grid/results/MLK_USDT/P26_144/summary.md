# EMA Hourly Continuation — MLK/USDT P26_144

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.4963 |
| net_win_rate | 0.3759 |
| gross_profit_factor | 0.6431 |
| gross_win_rate | 0.3782 |
| sharpe_ratio | -4.7976 |
| sortino_ratio | -1.3998 |
| max_drawdown | 0.8091 |
| cagr | -0.4790 |
| net_avg_win | 49.0854 |
| net_avg_loss | -59.5582 |
| avg_hold_time_bars | 20.5684 |
| exposure | 0.4012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

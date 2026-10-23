# EMA Hourly Continuation — MLK/USDT P12_55

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1289 |
| net_profit_factor | 0.3395 |
| net_win_rate | 0.3026 |
| gross_profit_factor | 0.6381 |
| gross_win_rate | 0.3134 |
| sharpe_ratio | -14.6400 |
| sortino_ratio | -7.5131 |
| max_drawdown | 0.9999 |
| cagr | -0.9773 |
| net_avg_win | 13.1805 |
| net_avg_loss | -16.8406 |
| avg_hold_time_bars | 6.7448 |
| exposure | 0.3934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LSK/USDT P55_89

**Symbol:** LSK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.4386 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -5.6691 |
| sortino_ratio | -1.9900 |
| max_drawdown | 0.9124 |
| cagr | -0.6143 |
| net_avg_win | 26.0045 |
| net_avg_loss | -48.3137 |
| avg_hold_time_bars | 4.9375 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

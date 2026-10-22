# EMA Hourly Continuation — JST/USDT P8_100

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.5095 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.0760 |
| sortino_ratio | -1.2906 |
| max_drawdown | 0.8140 |
| cagr | -0.4736 |
| net_avg_win | 33.1864 |
| net_avg_loss | -61.2285 |
| avg_hold_time_bars | 29.6390 |
| exposure | 0.6947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MLK/USDT P50_89

**Symbol:** MLK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.2201 |
| net_win_rate | 0.2621 |
| gross_profit_factor | 0.5018 |
| gross_win_rate | 0.2731 |
| sharpe_ratio | -14.2738 |
| sortino_ratio | -6.2252 |
| max_drawdown | 0.9997 |
| cagr | -0.9614 |
| net_avg_win | 11.8559 |
| net_avg_loss | -19.1328 |
| avg_hold_time_bars | 4.2048 |
| exposure | 0.1728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

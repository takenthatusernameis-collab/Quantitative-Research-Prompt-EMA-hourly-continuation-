# EMA Hourly Continuation — VET/USDT P26_144

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6390 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9364 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -3.1771 |
| sortino_ratio | -1.0111 |
| max_drawdown | 0.7222 |
| cagr | -0.3855 |
| net_avg_win | 50.1527 |
| net_avg_loss | -73.7508 |
| avg_hold_time_bars | 19.3638 |
| exposure | 0.4524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

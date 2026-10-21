# EMA Hourly Continuation — SKY/USDT P8_34

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.3200 |
| sortino_ratio | -1.3605 |
| max_drawdown | 0.7383 |
| cagr | -0.4633 |
| net_avg_win | 51.2267 |
| net_avg_loss | -71.5354 |
| avg_hold_time_bars | 7.8366 |
| exposure | 0.2915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

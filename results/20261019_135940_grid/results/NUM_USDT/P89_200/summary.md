# EMA Hourly Continuation — NUM/USDT P89_200

**Symbol:** NUM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5747 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7892 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -3.8472 |
| sortino_ratio | -1.0897 |
| max_drawdown | 0.7373 |
| cagr | -0.4014 |
| net_avg_win | 56.8940 |
| net_avg_loss | -73.4009 |
| avg_hold_time_bars | 13.2376 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

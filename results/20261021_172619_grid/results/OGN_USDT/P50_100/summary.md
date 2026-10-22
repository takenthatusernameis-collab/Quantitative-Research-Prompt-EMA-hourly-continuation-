# EMA Hourly Continuation — OGN/USDT P50_100

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5803 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8110 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -3.6879 |
| sortino_ratio | -1.1023 |
| max_drawdown | 0.7305 |
| cagr | -0.3993 |
| net_avg_win | 50.2772 |
| net_avg_loss | -70.6588 |
| avg_hold_time_bars | 9.2867 |
| exposure | 0.1862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

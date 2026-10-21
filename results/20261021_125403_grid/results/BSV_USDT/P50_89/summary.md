# EMA Hourly Continuation — BSV/USDT P50_89

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5697 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -3.4726 |
| sortino_ratio | -0.9828 |
| max_drawdown | 0.6800 |
| cagr | -0.3624 |
| net_avg_win | 50.3646 |
| net_avg_loss | -73.5292 |
| avg_hold_time_bars | 7.6505 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

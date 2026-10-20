# EMA Hourly Continuation — WEMIX/USDT P20_21

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1738 |
| net_profit_factor | 0.0547 |
| net_win_rate | 0.1703 |
| gross_profit_factor | 0.2314 |
| gross_win_rate | 0.2348 |
| sharpe_ratio | -26.8735 |
| sortino_ratio | -17.9322 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 1.9555 |
| net_avg_loss | -7.3362 |
| avg_hold_time_bars | 1.9453 |
| exposure | 0.1537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

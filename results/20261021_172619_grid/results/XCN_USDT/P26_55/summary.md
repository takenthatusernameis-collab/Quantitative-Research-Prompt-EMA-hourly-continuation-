# EMA Hourly Continuation — XCN/USDT P26_55

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6307 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8411 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -3.0412 |
| sortino_ratio | -0.8809 |
| max_drawdown | 0.6411 |
| cagr | -0.3331 |
| net_avg_win | 57.9992 |
| net_avg_loss | -76.4972 |
| avg_hold_time_bars | 7.5072 |
| exposure | 0.1413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

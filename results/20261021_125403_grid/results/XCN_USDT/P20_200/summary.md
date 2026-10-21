# EMA Hourly Continuation — XCN/USDT P20_200

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8355 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -2.1431 |
| sortino_ratio | -0.5497 |
| max_drawdown | 0.4776 |
| cagr | -0.2246 |
| net_avg_win | 73.7859 |
| net_avg_loss | -87.3092 |
| avg_hold_time_bars | 42.4164 |
| exposure | 0.6343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

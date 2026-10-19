# EMA Hourly Continuation — XCN/USDT P8_100

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.4708 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.7590 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -7.6060 |
| sortino_ratio | -3.2971 |
| max_drawdown | 0.9853 |
| cagr | -0.8125 |
| net_avg_win | 21.1189 |
| net_avg_loss | -33.4200 |
| avg_hold_time_bars | 13.3899 |
| exposure | 0.5916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XCH/USDT P26_55

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5932 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8067 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -3.4916 |
| sortino_ratio | -1.0905 |
| max_drawdown | 0.7188 |
| cagr | -0.3948 |
| net_avg_win | 48.5995 |
| net_avg_loss | -66.2246 |
| avg_hold_time_bars | 6.3971 |
| exposure | 0.1399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

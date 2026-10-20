# EMA Hourly Continuation — XCH/USDT P34_100

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.5125 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -4.8808 |
| sortino_ratio | -1.8447 |
| max_drawdown | 0.8999 |
| cagr | -0.5971 |
| net_avg_win | 27.3612 |
| net_avg_loss | -47.1097 |
| avg_hold_time_bars | 9.5041 |
| exposure | 0.3180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

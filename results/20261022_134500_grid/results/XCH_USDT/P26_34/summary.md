# EMA Hourly Continuation — XCH/USDT P26_34

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1299 |
| net_profit_factor | 0.1617 |
| net_win_rate | 0.3533 |
| gross_profit_factor | 0.6875 |
| gross_win_rate | 0.3918 |
| sharpe_ratio | -15.0259 |
| sortino_ratio | -7.8453 |
| max_drawdown | 1.0000 |
| cagr | -0.9846 |
| net_avg_win | 4.2019 |
| net_avg_loss | -14.2005 |
| avg_hold_time_bars | 1.8684 |
| exposure | 0.1103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

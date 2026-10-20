# EMA Hourly Continuation — XCH/USDT P89_200

**Symbol:** XCH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.5465 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8735 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -4.0578 |
| sortino_ratio | -1.2109 |
| max_drawdown | 0.7652 |
| cagr | -0.4384 |
| net_avg_win | 45.8838 |
| net_avg_loss | -69.1592 |
| avg_hold_time_bars | 9.8989 |
| exposure | 0.2002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XCH/USDT P26_55

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1107 |
| net_profit_factor | 0.3551 |
| net_win_rate | 0.4201 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -9.1480 |
| sortino_ratio | -4.2895 |
| max_drawdown | 0.9953 |
| cagr | -0.8813 |
| net_avg_win | 11.7834 |
| net_avg_loss | -24.0372 |
| avg_hold_time_bars | 3.8591 |
| exposure | 0.1942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XCH/USDT P20_26

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1451 |
| net_profit_factor | 0.1499 |
| net_win_rate | 0.3453 |
| gross_profit_factor | 0.6894 |
| gross_win_rate | 0.3859 |
| sharpe_ratio | -16.4671 |
| sortino_ratio | -9.1413 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 3.5191 |
| net_avg_loss | -12.3821 |
| avg_hold_time_bars | 1.9876 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ILV/USDT P55_100

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.6118 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 1.0056 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -4.1755 |
| sortino_ratio | -1.4449 |
| max_drawdown | 0.8230 |
| cagr | -0.4982 |
| net_avg_win | 45.3558 |
| net_avg_loss | -68.6142 |
| avg_hold_time_bars | 5.8992 |
| exposure | 0.1595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

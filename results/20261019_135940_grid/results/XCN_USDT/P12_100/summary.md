# EMA Hourly Continuation — XCN/USDT P12_100

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 906 |
| net_profit_factor | 0.4515 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7640 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -7.4944 |
| sortino_ratio | -3.1336 |
| max_drawdown | 0.9818 |
| cagr | -0.7951 |
| net_avg_win | 20.9304 |
| net_avg_loss | -34.4084 |
| avg_hold_time_bars | 12.7020 |
| exposure | 0.5231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

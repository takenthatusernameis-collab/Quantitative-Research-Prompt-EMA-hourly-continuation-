# EMA Hourly Continuation — XCN/USDT P21_200

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5600 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8402 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -4.2279 |
| sortino_ratio | -1.3420 |
| max_drawdown | 0.8036 |
| cagr | -0.4748 |
| net_avg_win | 44.5503 |
| net_avg_loss | -64.1463 |
| avg_hold_time_bars | 26.4074 |
| exposure | 0.6158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

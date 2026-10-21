# EMA Hourly Continuation — XCN/USDT P21_34

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.7465 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0568 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.4700 |
| sortino_ratio | -0.3367 |
| max_drawdown | 0.3402 |
| cagr | -0.1426 |
| net_avg_win | 72.5710 |
| net_avg_loss | -102.7532 |
| avg_hold_time_bars | 6.6917 |
| exposure | 0.0770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

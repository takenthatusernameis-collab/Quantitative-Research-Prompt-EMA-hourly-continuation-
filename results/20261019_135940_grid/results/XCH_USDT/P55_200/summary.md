# EMA Hourly Continuation — XCH/USDT P55_200

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.5699 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.7313 |
| sortino_ratio | -1.1231 |
| max_drawdown | 0.7545 |
| cagr | -0.4270 |
| net_avg_win | 45.9791 |
| net_avg_loss | -69.7530 |
| avg_hold_time_bars | 17.0962 |
| exposure | 0.3637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

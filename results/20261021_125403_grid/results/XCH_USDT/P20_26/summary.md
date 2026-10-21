# EMA Hourly Continuation — XCH/USDT P20_26

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 181 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.7990 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -2.3293 |
| sortino_ratio | -0.4468 |
| max_drawdown | 0.4129 |
| cagr | -0.1856 |
| net_avg_win | 68.1966 |
| net_avg_loss | -93.9011 |
| avg_hold_time_bars | 5.1271 |
| exposure | 0.0422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

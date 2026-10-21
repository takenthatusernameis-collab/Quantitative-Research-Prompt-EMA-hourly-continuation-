# EMA Hourly Continuation — XCH/USDT P21_89

**Symbol:** XCH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.8158 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.3616 |
| sortino_ratio | -0.4539 |
| max_drawdown | 0.4587 |
| cagr | -0.1902 |
| net_avg_win | 66.2447 |
| net_avg_loss | -84.5868 |
| avg_hold_time_bars | 16.0816 |
| exposure | 0.3940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

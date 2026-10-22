# EMA Hourly Continuation — XCN/USDT P21_55

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.3480 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.6879 |
| gross_win_rate | 0.4143 |
| sharpe_ratio | -10.5974 |
| sortino_ratio | -5.0866 |
| max_drawdown | 0.9985 |
| cagr | -0.9250 |
| net_avg_win | 11.8145 |
| net_avg_loss | -21.5681 |
| avg_hold_time_bars | 4.7313 |
| exposure | 0.2497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

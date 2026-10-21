# EMA Hourly Continuation — XCN/USDT P21_55

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8982 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -2.8015 |
| sortino_ratio | -0.8753 |
| max_drawdown | 0.6461 |
| cagr | -0.3315 |
| net_avg_win | 60.4401 |
| net_avg_loss | -78.2816 |
| avg_hold_time_bars | 8.7312 |
| exposure | 0.1905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

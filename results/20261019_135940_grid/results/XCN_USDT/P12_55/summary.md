# EMA Hourly Continuation — XCN/USDT P12_55

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.3801 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.6553 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -9.9593 |
| sortino_ratio | -4.8621 |
| max_drawdown | 0.9980 |
| cagr | -0.9153 |
| net_avg_win | 12.4393 |
| net_avg_loss | -22.2681 |
| avg_hold_time_bars | 6.8930 |
| exposure | 0.3807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

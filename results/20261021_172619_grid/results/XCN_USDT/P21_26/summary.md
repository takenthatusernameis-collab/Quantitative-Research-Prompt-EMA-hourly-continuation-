# EMA Hourly Continuation — XCN/USDT P21_26

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.9605 |
| net_win_rate | 0.5779 |
| gross_profit_factor | 1.3542 |
| gross_win_rate | 0.5779 |
| sharpe_ratio | -0.1257 |
| sortino_ratio | -0.0228 |
| max_drawdown | 0.1620 |
| cagr | -0.0129 |
| net_avg_win | 87.3971 |
| net_avg_loss | -124.5921 |
| avg_hold_time_bars | 6.0130 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

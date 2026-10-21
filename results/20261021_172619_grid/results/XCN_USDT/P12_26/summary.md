# EMA Hourly Continuation — XCN/USDT P12_26

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.2193 |
| sortino_ratio | -0.6219 |
| max_drawdown | 0.5162 |
| cagr | -0.2477 |
| net_avg_win | 61.0813 |
| net_avg_loss | -85.5195 |
| avg_hold_time_bars | 6.1257 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

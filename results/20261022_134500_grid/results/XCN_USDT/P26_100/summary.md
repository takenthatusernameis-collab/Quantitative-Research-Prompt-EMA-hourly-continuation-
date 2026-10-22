# EMA Hourly Continuation — XCN/USDT P26_100

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 799 |
| net_profit_factor | 0.4332 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 0.7779 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -7.5451 |
| sortino_ratio | -2.9662 |
| max_drawdown | 0.9778 |
| cagr | -0.7798 |
| net_avg_win | 22.5742 |
| net_avg_loss | -36.8552 |
| avg_hold_time_bars | 10.0588 |
| exposure | 0.3653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

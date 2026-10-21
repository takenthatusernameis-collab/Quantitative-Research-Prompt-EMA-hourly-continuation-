# EMA Hourly Continuation — XCN/USDT P12_34

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.7928 |
| sortino_ratio | -0.9134 |
| max_drawdown | 0.6587 |
| cagr | -0.3424 |
| net_avg_win | 56.4481 |
| net_avg_loss | -75.7445 |
| avg_hold_time_bars | 7.4504 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

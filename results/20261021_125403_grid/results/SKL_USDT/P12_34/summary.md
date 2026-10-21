# EMA Hourly Continuation — SKL/USDT P12_34

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.7574 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0124 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.6593 |
| sortino_ratio | -0.9599 |
| max_drawdown | 0.7030 |
| cagr | -0.3564 |
| net_avg_win | 66.9818 |
| net_avg_loss | -85.4227 |
| avg_hold_time_bars | 6.4661 |
| exposure | 0.1866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

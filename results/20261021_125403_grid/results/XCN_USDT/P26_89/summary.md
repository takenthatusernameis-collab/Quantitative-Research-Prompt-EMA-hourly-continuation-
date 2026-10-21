# EMA Hourly Continuation — XCN/USDT P26_89

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6970 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.5047 |
| sortino_ratio | -0.7411 |
| max_drawdown | 0.5829 |
| cagr | -0.2888 |
| net_avg_win | 65.4867 |
| net_avg_loss | -82.5191 |
| avg_hold_time_bars | 15.8727 |
| exposure | 0.3117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

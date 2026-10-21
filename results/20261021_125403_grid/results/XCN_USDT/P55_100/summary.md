# EMA Hourly Continuation — XCN/USDT P55_100

**Symbol:** XCN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7103 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9528 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.8835 |
| sortino_ratio | -0.4692 |
| max_drawdown | 0.4273 |
| cagr | -0.1933 |
| net_avg_win | 69.0677 |
| net_avg_loss | -92.8493 |
| avg_hold_time_bars | 8.6007 |
| exposure | 0.1185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

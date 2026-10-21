# EMA Hourly Continuation — XCH/USDT P12_100

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.8245 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.3163 |
| sortino_ratio | -0.4403 |
| max_drawdown | 0.4146 |
| cagr | -0.1863 |
| net_avg_win | 69.0690 |
| net_avg_loss | -85.3180 |
| avg_hold_time_bars | 22.8349 |
| exposure | 0.5657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XCN/USDT P34_144

**Symbol:** XCN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.4994 |
| net_win_rate | 0.4222 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -6.0557 |
| sortino_ratio | -2.1363 |
| max_drawdown | 0.9281 |
| cagr | -0.6491 |
| net_avg_win | 34.7940 |
| net_avg_loss | -50.9182 |
| avg_hold_time_bars | 14.2222 |
| exposure | 0.4073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

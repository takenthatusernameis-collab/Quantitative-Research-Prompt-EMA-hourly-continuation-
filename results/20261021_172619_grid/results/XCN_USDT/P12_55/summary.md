# EMA Hourly Continuation — XCN/USDT P12_55

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -2.7271 |
| sortino_ratio | -0.9447 |
| max_drawdown | 0.6708 |
| cagr | -0.3529 |
| net_avg_win | 54.0803 |
| net_avg_loss | -70.4652 |
| avg_hold_time_bars | 12.0169 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

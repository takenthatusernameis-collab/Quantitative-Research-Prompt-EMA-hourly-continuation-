# EMA Hourly Continuation — XNO/USDT P12_100

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 888 |
| net_profit_factor | 0.5433 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -7.0078 |
| sortino_ratio | -2.9392 |
| max_drawdown | 0.9720 |
| cagr | -0.7569 |
| net_avg_win | 32.0079 |
| net_avg_loss | -40.3571 |
| avg_hold_time_bars | 12.7691 |
| exposure | 0.5154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

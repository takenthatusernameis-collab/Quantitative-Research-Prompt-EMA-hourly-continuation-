# EMA Hourly Continuation — T/USDT P20_144

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7790 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0290 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.5445 |
| sortino_ratio | -0.4411 |
| max_drawdown | 0.4076 |
| cagr | -0.1848 |
| net_avg_win | 69.9485 |
| net_avg_loss | -92.5218 |
| avg_hold_time_bars | 28.2725 |
| exposure | 0.5118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

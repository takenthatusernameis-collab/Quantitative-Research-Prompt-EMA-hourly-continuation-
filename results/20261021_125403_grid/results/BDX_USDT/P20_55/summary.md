# EMA Hourly Continuation — BDX/USDT P20_55

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.4477 |
| net_win_rate | 0.4109 |
| gross_profit_factor | 0.7342 |
| gross_win_rate | 0.4109 |
| sharpe_ratio | -4.7888 |
| sortino_ratio | -1.2473 |
| max_drawdown | 0.7815 |
| cagr | -0.4424 |
| net_avg_win | 45.8507 |
| net_avg_loss | -71.4332 |
| avg_hold_time_bars | 9.6163 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

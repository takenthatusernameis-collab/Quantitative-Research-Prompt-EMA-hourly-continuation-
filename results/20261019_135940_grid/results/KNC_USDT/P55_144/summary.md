# EMA Hourly Continuation — KNC/USDT P55_144

**Symbol:** KNC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9215 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -3.5326 |
| sortino_ratio | -1.0702 |
| max_drawdown | 0.7507 |
| cagr | -0.4004 |
| net_avg_win | 45.5723 |
| net_avg_loss | -70.4411 |
| avg_hold_time_bars | 13.0946 |
| exposure | 0.2768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

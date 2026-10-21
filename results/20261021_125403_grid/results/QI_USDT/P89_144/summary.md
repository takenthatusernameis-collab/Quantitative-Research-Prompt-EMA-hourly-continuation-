# EMA Hourly Continuation — QI/USDT P89_144

**Symbol:** QI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.7209 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -3.1694 |
| sortino_ratio | -0.7588 |
| max_drawdown | 0.5918 |
| cagr | -0.2951 |
| net_avg_win | 50.4288 |
| net_avg_loss | -74.9348 |
| avg_hold_time_bars | 7.9261 |
| exposure | 0.1019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

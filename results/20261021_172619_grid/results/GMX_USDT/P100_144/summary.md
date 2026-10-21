# EMA Hourly Continuation — GMX/USDT P100_144

**Symbol:** GMX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.5378 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.7742 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -3.5277 |
| sortino_ratio | -0.9005 |
| max_drawdown | 0.6478 |
| cagr | -0.3400 |
| net_avg_win | 54.6324 |
| net_avg_loss | -77.0199 |
| avg_hold_time_bars | 5.8344 |
| exposure | 0.0849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

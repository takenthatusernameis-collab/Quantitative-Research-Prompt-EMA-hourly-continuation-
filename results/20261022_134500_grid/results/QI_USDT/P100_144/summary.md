# EMA Hourly Continuation — QI/USDT P100_144

**Symbol:** QI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.4096 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -5.1218 |
| sortino_ratio | -1.5884 |
| max_drawdown | 0.8557 |
| cagr | -0.5338 |
| net_avg_win | 27.3107 |
| net_avg_loss | -54.8033 |
| avg_hold_time_bars | 4.5094 |
| exposure | 0.0981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

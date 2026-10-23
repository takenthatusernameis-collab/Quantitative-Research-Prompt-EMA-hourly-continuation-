# EMA Hourly Continuation — LPT/USDT P20_55

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.5097 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -7.4346 |
| sortino_ratio | -3.3122 |
| max_drawdown | 0.9843 |
| cagr | -0.8027 |
| net_avg_win | 23.4886 |
| net_avg_loss | -35.1100 |
| avg_hold_time_bars | 5.6610 |
| exposure | 0.2589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

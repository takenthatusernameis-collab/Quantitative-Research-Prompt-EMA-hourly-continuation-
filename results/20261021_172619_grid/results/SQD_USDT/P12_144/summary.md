# EMA Hourly Continuation — SQD/USDT P12_144

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.9168 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0467 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -0.4978 |
| sortino_ratio | -0.1498 |
| max_drawdown | 0.2809 |
| cagr | -0.0718 |
| net_avg_win | 83.6679 |
| net_avg_loss | -96.5771 |
| avg_hold_time_bars | 29.9009 |
| exposure | 0.5959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

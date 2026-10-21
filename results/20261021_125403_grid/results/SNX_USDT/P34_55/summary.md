# EMA Hourly Continuation — SNX/USDT P34_55

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7350 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.7509 |
| sortino_ratio | -0.4558 |
| max_drawdown | 0.4114 |
| cagr | -0.1871 |
| net_avg_win | 68.0173 |
| net_avg_loss | -94.2429 |
| avg_hold_time_bars | 5.8450 |
| exposure | 0.0870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

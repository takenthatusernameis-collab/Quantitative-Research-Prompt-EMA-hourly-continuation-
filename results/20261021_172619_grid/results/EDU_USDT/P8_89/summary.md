# EMA Hourly Continuation — EDU/USDT P8_89

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.7652 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.0224 |
| sortino_ratio | -0.6788 |
| max_drawdown | 0.5708 |
| cagr | -0.2696 |
| net_avg_win | 66.5357 |
| net_avg_loss | -80.3603 |
| avg_hold_time_bars | 25.4624 |
| exposure | 0.6429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

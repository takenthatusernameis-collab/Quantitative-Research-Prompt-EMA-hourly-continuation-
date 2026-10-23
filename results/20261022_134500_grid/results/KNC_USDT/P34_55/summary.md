# EMA Hourly Continuation — KNC/USDT P34_55

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 799 |
| net_profit_factor | 0.4268 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.8719 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -8.1850 |
| sortino_ratio | -3.2956 |
| max_drawdown | 0.9842 |
| cagr | -0.8065 |
| net_avg_win | 20.9904 |
| net_avg_loss | -38.1421 |
| avg_hold_time_bars | 4.3642 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

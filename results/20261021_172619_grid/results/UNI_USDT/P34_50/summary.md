# EMA Hourly Continuation — UNI/USDT P34_50

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.0819 |
| sortino_ratio | -0.4428 |
| max_drawdown | 0.4041 |
| cagr | -0.1833 |
| net_avg_win | 66.8843 |
| net_avg_loss | -91.3812 |
| avg_hold_time_bars | 5.6892 |
| exposure | 0.0574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

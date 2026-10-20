# EMA Hourly Continuation — XPR/USDT P34_55

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.2700 |
| net_win_rate | 0.3613 |
| gross_profit_factor | 0.6458 |
| gross_win_rate | 0.3871 |
| sharpe_ratio | -11.2715 |
| sortino_ratio | -4.5344 |
| max_drawdown | 0.9980 |
| cagr | -0.9151 |
| net_avg_win | 13.1792 |
| net_avg_loss | -27.6157 |
| avg_hold_time_bars | 4.3097 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XPR/USDT P34_100

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.3801 |
| net_win_rate | 0.4055 |
| gross_profit_factor | 0.7013 |
| gross_win_rate | 0.4116 |
| sharpe_ratio | -7.5991 |
| sortino_ratio | -2.7475 |
| max_drawdown | 0.9699 |
| cagr | -0.7504 |
| net_avg_win | 22.3421 |
| net_avg_loss | -40.0934 |
| avg_hold_time_bars | 7.5976 |
| exposure | 0.2265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

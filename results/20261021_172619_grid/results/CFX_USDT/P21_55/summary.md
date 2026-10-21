# EMA Hourly Continuation — CFX/USDT P21_55

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6140 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -3.2921 |
| sortino_ratio | -1.0401 |
| max_drawdown | 0.7223 |
| cagr | -0.3797 |
| net_avg_win | 49.8234 |
| net_avg_loss | -67.2714 |
| avg_hold_time_bars | 8.3435 |
| exposure | 0.1866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

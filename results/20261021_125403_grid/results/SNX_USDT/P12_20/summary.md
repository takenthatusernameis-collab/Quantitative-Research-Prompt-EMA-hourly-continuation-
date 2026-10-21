# EMA Hourly Continuation — SNX/USDT P12_20

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7515 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0898 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.7719 |
| sortino_ratio | -0.4787 |
| max_drawdown | 0.4909 |
| cagr | -0.1953 |
| net_avg_win | 70.1076 |
| net_avg_loss | -99.8736 |
| avg_hold_time_bars | 4.8011 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

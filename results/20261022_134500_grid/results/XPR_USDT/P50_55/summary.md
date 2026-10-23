# EMA Hourly Continuation — XPR/USDT P50_55

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.1073 |
| net_win_rate | 0.2520 |
| gross_profit_factor | 0.4155 |
| gross_win_rate | 0.2900 |
| sharpe_ratio | -15.5731 |
| sortino_ratio | -6.7595 |
| max_drawdown | 0.9999 |
| cagr | -0.9797 |
| net_avg_win | 6.4613 |
| net_avg_loss | -20.2921 |
| avg_hold_time_bars | 1.9770 |
| exposure | 0.0663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

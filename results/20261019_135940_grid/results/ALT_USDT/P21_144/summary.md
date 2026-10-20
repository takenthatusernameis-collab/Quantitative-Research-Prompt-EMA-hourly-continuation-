# EMA Hourly Continuation — ALT/USDT P21_144

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8686 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -2.7098 |
| sortino_ratio | -0.8295 |
| max_drawdown | 0.6387 |
| cagr | -0.3210 |
| net_avg_win | 59.0294 |
| net_avg_loss | -76.3421 |
| avg_hold_time_bars | 26.2094 |
| exposure | 0.5575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

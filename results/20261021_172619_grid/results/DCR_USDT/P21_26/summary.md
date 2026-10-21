# EMA Hourly Continuation — DCR/USDT P21_26

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -2.9719 |
| sortino_ratio | -0.7631 |
| max_drawdown | 0.6070 |
| cagr | -0.2956 |
| net_avg_win | 54.8045 |
| net_avg_loss | -87.9183 |
| avg_hold_time_bars | 4.7469 |
| exposure | 0.0687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

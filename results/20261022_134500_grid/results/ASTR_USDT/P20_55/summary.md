# EMA Hourly Continuation — ASTR/USDT P20_55

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.4927 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -6.5186 |
| sortino_ratio | -2.7058 |
| max_drawdown | 0.9679 |
| cagr | -0.7401 |
| net_avg_win | 22.8444 |
| net_avg_loss | -40.2856 |
| avg_hold_time_bars | 6.1719 |
| exposure | 0.2469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

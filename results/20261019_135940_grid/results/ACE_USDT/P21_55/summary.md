# EMA Hourly Continuation — ACE/USDT P21_55

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.5782 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.1695 |
| sortino_ratio | -1.6152 |
| max_drawdown | 0.8586 |
| cagr | -0.5339 |
| net_avg_win | 31.8229 |
| net_avg_loss | -52.7410 |
| avg_hold_time_bars | 7.3391 |
| exposure | 0.2498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — NMR/USDT P21_55

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.6847 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9235 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -3.3708 |
| sortino_ratio | -1.1644 |
| max_drawdown | 0.7460 |
| cagr | -0.4136 |
| net_avg_win | 58.0909 |
| net_avg_loss | -75.2930 |
| avg_hold_time_bars | 7.9847 |
| exposure | 0.2130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

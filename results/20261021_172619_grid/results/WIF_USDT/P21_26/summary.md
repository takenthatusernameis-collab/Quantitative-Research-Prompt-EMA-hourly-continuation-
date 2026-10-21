# EMA Hourly Continuation — WIF/USDT P21_26

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 125 |
| net_profit_factor | 0.8782 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.1212 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.4746 |
| sortino_ratio | -0.0765 |
| max_drawdown | 0.2052 |
| cagr | -0.0356 |
| net_avg_win | 95.1108 |
| net_avg_loss | -121.1525 |
| avg_hold_time_bars | 5.1600 |
| exposure | 0.0293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ACE/USDT P100_200

**Symbol:** ACE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6549 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9592 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -2.4223 |
| sortino_ratio | -0.6432 |
| max_drawdown | 0.5346 |
| cagr | -0.2591 |
| net_avg_win | 60.2941 |
| net_avg_loss | -83.1114 |
| avg_hold_time_bars | 10.9318 |
| exposure | 0.1741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

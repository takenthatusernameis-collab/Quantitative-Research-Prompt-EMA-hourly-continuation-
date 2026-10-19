# EMA Hourly Continuation — BTT/USDT P21_144

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.4784 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -6.1604 |
| sortino_ratio | -1.8371 |
| max_drawdown | 0.9042 |
| cagr | -0.6070 |
| net_avg_win | 45.3122 |
| net_avg_loss | -65.4125 |
| avg_hold_time_bars | 28.4554 |
| exposure | 0.5795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

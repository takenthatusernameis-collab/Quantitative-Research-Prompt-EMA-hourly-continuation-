# EMA Hourly Continuation — SUN/USDT P100_200

**Symbol:** SUN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.5047 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8680 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.7779 |
| sortino_ratio | -0.8669 |
| max_drawdown | 0.6561 |
| cagr | -0.3369 |
| net_avg_win | 56.6809 |
| net_avg_loss | -91.1026 |
| avg_hold_time_bars | 16.7066 |
| exposure | 0.1958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

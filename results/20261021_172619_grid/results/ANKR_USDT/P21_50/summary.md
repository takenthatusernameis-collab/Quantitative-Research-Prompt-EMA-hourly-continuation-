# EMA Hourly Continuation — ANKR/USDT P21_50

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -4.0864 |
| sortino_ratio | -1.3945 |
| max_drawdown | 0.8066 |
| cagr | -0.4746 |
| net_avg_win | 52.3977 |
| net_avg_loss | -69.3485 |
| avg_hold_time_bars | 9.4073 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

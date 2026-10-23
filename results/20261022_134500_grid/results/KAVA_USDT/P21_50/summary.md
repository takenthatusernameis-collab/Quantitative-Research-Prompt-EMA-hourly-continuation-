# EMA Hourly Continuation — KAVA/USDT P21_50

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.5069 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -9.4520 |
| sortino_ratio | -4.3267 |
| max_drawdown | 0.9961 |
| cagr | -0.8884 |
| net_avg_win | 23.0095 |
| net_avg_loss | -33.4970 |
| avg_hold_time_bars | 5.1708 |
| exposure | 0.2463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

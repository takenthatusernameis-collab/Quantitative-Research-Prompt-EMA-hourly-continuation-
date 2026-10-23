# EMA Hourly Continuation — REZ/USDT P100_200

**Symbol:** REZ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6460 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.8258 |
| sortino_ratio | -0.7892 |
| max_drawdown | 0.6211 |
| cagr | -0.3102 |
| net_avg_win | 61.2616 |
| net_avg_loss | -82.8095 |
| avg_hold_time_bars | 9.8906 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

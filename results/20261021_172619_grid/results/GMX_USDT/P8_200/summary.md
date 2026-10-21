# EMA Hourly Continuation — GMX/USDT P8_200

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.8243 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.3165 |
| sortino_ratio | -0.3707 |
| max_drawdown | 0.4624 |
| cagr | -0.1587 |
| net_avg_win | 85.6048 |
| net_avg_loss | -101.7369 |
| avg_hold_time_bars | 42.1974 |
| exposure | 0.7480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

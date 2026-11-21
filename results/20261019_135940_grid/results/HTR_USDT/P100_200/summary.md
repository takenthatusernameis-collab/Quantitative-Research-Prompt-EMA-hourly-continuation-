# EMA Hourly Continuation — HTR/USDT P100_200

**Symbol:** HTR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5331 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.8477 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -5.2666 |
| sortino_ratio | -1.6188 |
| max_drawdown | 0.8854 |
| cagr | -0.5698 |
| net_avg_win | 46.7217 |
| net_avg_loss | -66.1157 |
| avg_hold_time_bars | 7.7940 |
| exposure | 0.1771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

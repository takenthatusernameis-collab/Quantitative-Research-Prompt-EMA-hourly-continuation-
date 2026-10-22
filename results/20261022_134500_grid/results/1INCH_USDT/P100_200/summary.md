# EMA Hourly Continuation — 1INCH/USDT P100_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5523 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -4.1723 |
| sortino_ratio | -1.1589 |
| max_drawdown | 0.7804 |
| cagr | -0.4429 |
| net_avg_win | 50.7912 |
| net_avg_loss | -80.7371 |
| avg_hold_time_bars | 9.2875 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

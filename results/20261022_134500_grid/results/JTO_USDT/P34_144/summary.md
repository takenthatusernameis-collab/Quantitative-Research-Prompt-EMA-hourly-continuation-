# EMA Hourly Continuation — JTO/USDT P34_144

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6382 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8600 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.3201 |
| sortino_ratio | -1.0582 |
| max_drawdown | 0.7340 |
| cagr | -0.3964 |
| net_avg_win | 53.4895 |
| net_avg_loss | -70.6869 |
| avg_hold_time_bars | 15.9073 |
| exposure | 0.3745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

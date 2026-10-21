# EMA Hourly Continuation — TRX/USDT P50_100

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.4496 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 1.0682 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -4.4233 |
| sortino_ratio | -1.1240 |
| max_drawdown | 0.7292 |
| cagr | -0.4041 |
| net_avg_win | 40.9871 |
| net_avg_loss | -85.2805 |
| avg_hold_time_bars | 10.1500 |
| exposure | 0.1384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

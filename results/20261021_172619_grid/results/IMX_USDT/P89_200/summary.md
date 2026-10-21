# EMA Hourly Continuation — IMX/USDT P89_200

**Symbol:** IMX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9076 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1323 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.4677 |
| sortino_ratio | -0.1143 |
| max_drawdown | 0.1647 |
| cagr | -0.0540 |
| net_avg_win | 83.9016 |
| net_avg_loss | -105.5525 |
| avg_hold_time_bars | 14.6341 |
| exposure | 0.1901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

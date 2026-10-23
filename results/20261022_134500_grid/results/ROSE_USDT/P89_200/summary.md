# EMA Hourly Continuation — ROSE/USDT P89_200

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6510 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.4600 |
| sortino_ratio | -0.6859 |
| max_drawdown | 0.5698 |
| cagr | -0.2807 |
| net_avg_win | 53.8426 |
| net_avg_loss | -81.8647 |
| avg_hold_time_bars | 11.1888 |
| exposure | 0.1994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

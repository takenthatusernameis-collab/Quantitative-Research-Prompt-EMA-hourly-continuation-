# EMA Hourly Continuation — METIS/USDT P8_34

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.6873 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -3.3521 |
| sortino_ratio | -1.3195 |
| max_drawdown | 0.7882 |
| cagr | -0.4545 |
| net_avg_win | 47.8523 |
| net_avg_loss | -61.8710 |
| avg_hold_time_bars | 9.3722 |
| exposure | 0.3250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

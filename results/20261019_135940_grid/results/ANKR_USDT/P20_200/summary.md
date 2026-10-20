# EMA Hourly Continuation — ANKR/USDT P20_200

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6824 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -2.5566 |
| sortino_ratio | -0.6888 |
| max_drawdown | 0.5695 |
| cagr | -0.2777 |
| net_avg_win | 69.3236 |
| net_avg_loss | -93.4852 |
| avg_hold_time_bars | 41.9889 |
| exposure | 0.6890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

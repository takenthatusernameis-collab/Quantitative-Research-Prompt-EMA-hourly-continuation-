# EMA Hourly Continuation — ANKR/USDT P89_200

**Symbol:** ANKR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -3.1991 |
| sortino_ratio | -0.9197 |
| max_drawdown | 0.6676 |
| cagr | -0.3515 |
| net_avg_win | 53.0969 |
| net_avg_loss | -79.9845 |
| avg_hold_time_bars | 14.5868 |
| exposure | 0.2712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

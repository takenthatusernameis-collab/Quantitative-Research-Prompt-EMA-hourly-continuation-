# EMA Hourly Continuation — GALA/USDT P12_200

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.6916 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9268 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.9139 |
| sortino_ratio | -0.4733 |
| max_drawdown | 0.4480 |
| cagr | -0.2024 |
| net_avg_win | 64.7616 |
| net_avg_loss | -87.7915 |
| avg_hold_time_bars | 55.1258 |
| exposure | 0.7768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

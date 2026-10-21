# EMA Hourly Continuation — COMP/USDT P50_200

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7156 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -1.7255 |
| sortino_ratio | -0.4490 |
| max_drawdown | 0.4302 |
| cagr | -0.1868 |
| net_avg_win | 62.9089 |
| net_avg_loss | -83.7774 |
| avg_hold_time_bars | 25.5602 |
| exposure | 0.3857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

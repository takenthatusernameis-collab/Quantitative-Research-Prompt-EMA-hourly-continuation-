# EMA Hourly Continuation — RENDER/USDT P89_200

**Symbol:** RENDER/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.1124 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -1.7556 |
| sortino_ratio | -0.4895 |
| max_drawdown | 0.4557 |
| cagr | -0.2071 |
| net_avg_win | 69.1058 |
| net_avg_loss | -101.0789 |
| avg_hold_time_bars | 12.6235 |
| exposure | 0.2212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

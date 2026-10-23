# EMA Hourly Continuation — TRADE/USDT P8_144

**Symbol:** TRADE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7523 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.9642 |
| sortino_ratio | -0.5934 |
| max_drawdown | 0.5411 |
| cagr | -0.2444 |
| net_avg_win | 70.0668 |
| net_avg_loss | -86.4297 |
| avg_hold_time_bars | 34.5187 |
| exposure | 0.7139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

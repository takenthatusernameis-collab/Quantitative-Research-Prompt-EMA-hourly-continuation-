# EMA Hourly Continuation — MOVR/USDT P50_55

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 145 |
| net_profit_factor | 0.7578 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.1001 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -1.0212 |
| sortino_ratio | -0.1777 |
| max_drawdown | 0.2071 |
| cagr | -0.0775 |
| net_avg_win | 75.4813 |
| net_avg_loss | -109.7087 |
| avg_hold_time_bars | 4.8138 |
| exposure | 0.0317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

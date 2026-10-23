# EMA Hourly Continuation — POPCAT/USDT P12_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7675 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7885 |
| sortino_ratio | -0.5157 |
| max_drawdown | 0.4597 |
| cagr | -0.2175 |
| net_avg_win | 76.2862 |
| net_avg_loss | -97.2101 |
| avg_hold_time_bars | 38.0944 |
| exposure | 0.7245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

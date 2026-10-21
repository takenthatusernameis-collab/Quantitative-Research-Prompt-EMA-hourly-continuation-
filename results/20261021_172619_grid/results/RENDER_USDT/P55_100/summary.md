# EMA Hourly Continuation — RENDER/USDT P55_100

**Symbol:** RENDER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -2.1944 |
| sortino_ratio | -0.5948 |
| max_drawdown | 0.4798 |
| cagr | -0.2394 |
| net_avg_win | 73.6586 |
| net_avg_loss | -93.2577 |
| avg_hold_time_bars | 7.9100 |
| exposure | 0.1298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PUFFER/USDT P8_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8950 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0444 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -0.7202 |
| sortino_ratio | -0.2284 |
| max_drawdown | 0.2647 |
| cagr | -0.1046 |
| net_avg_win | 84.6933 |
| net_avg_loss | -99.5888 |
| avg_hold_time_bars | 29.4821 |
| exposure | 0.6540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DOGS/USDT P55_144

**Symbol:** DOGS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8763 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0690 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -0.8001 |
| sortino_ratio | -0.2105 |
| max_drawdown | 0.3247 |
| cagr | -0.0946 |
| net_avg_win | 92.1215 |
| net_avg_loss | -111.9364 |
| avg_hold_time_bars | 17.1220 |
| exposure | 0.2607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

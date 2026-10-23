# EMA Hourly Continuation — CFG/USDT P21_144

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6212 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -2.9650 |
| sortino_ratio | -0.8352 |
| max_drawdown | 0.6519 |
| cagr | -0.3292 |
| net_avg_win | 57.0409 |
| net_avg_loss | -75.2841 |
| avg_hold_time_bars | 34.0297 |
| exposure | 0.6249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

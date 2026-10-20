# EMA Hourly Continuation — CFG/USDT P55_144

**Symbol:** CFG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.5800 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8324 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -3.6396 |
| sortino_ratio | -1.1943 |
| max_drawdown | 0.7648 |
| cagr | -0.4334 |
| net_avg_win | 42.1365 |
| net_avg_loss | -61.3248 |
| avg_hold_time_bars | 9.4044 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

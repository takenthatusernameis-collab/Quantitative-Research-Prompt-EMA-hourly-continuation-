# EMA Hourly Continuation — CETUS/USDT P55_144

**Symbol:** CETUS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.9711 |
| net_win_rate | 0.5439 |
| gross_profit_factor | 1.1853 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -0.1322 |
| sortino_ratio | -0.0353 |
| max_drawdown | 0.2461 |
| cagr | -0.0220 |
| net_avg_win | 98.5067 |
| net_avg_loss | -120.9477 |
| avg_hold_time_bars | 16.0731 |
| exposure | 0.2488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

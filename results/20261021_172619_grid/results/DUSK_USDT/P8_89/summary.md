# EMA Hourly Continuation — DUSK/USDT P8_89

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -1.9216 |
| sortino_ratio | -0.6288 |
| max_drawdown | 0.6140 |
| cagr | -0.2528 |
| net_avg_win | 81.0254 |
| net_avg_loss | -92.4497 |
| avg_hold_time_bars | 27.0794 |
| exposure | 0.6511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

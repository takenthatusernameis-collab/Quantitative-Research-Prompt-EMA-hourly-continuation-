# EMA Hourly Continuation — POPCAT/USDT P55_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6616 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8349 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -2.4489 |
| sortino_ratio | -0.6783 |
| max_drawdown | 0.5114 |
| cagr | -0.2676 |
| net_avg_win | 63.8428 |
| net_avg_loss | -82.2406 |
| avg_hold_time_bars | 6.8252 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

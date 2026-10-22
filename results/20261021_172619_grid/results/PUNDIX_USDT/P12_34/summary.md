# EMA Hourly Continuation — PUNDIX/USDT P12_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.6101 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -4.3057 |
| sortino_ratio | -1.6110 |
| max_drawdown | 0.8510 |
| cagr | -0.5224 |
| net_avg_win | 41.2561 |
| net_avg_loss | -59.4471 |
| avg_hold_time_bars | 7.9488 |
| exposure | 0.2471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

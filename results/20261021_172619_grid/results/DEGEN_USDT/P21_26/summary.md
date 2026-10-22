# EMA Hourly Continuation — DEGEN/USDT P21_26

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.7205 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.5103 |
| sortino_ratio | -0.3170 |
| max_drawdown | 0.3128 |
| cagr | -0.1356 |
| net_avg_win | 75.1340 |
| net_avg_loss | -99.5392 |
| avg_hold_time_bars | 6.0093 |
| exposure | 0.0588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

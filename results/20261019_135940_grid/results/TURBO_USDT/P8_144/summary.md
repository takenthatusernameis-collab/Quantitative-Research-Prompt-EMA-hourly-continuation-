# EMA Hourly Continuation — TURBO/USDT P8_144

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6172 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8376 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -3.7352 |
| sortino_ratio | -1.1599 |
| max_drawdown | 0.7035 |
| cagr | -0.4294 |
| net_avg_win | 60.5277 |
| net_avg_loss | -79.1456 |
| avg_hold_time_bars | 32.3883 |
| exposure | 0.7280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

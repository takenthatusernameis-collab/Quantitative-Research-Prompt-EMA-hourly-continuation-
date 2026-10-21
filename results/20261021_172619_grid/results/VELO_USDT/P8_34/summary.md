# EMA Hourly Continuation — VELO/USDT P8_34

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.8028 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 0.9862 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.6287 |
| sortino_ratio | -0.6007 |
| max_drawdown | 0.5419 |
| cagr | -0.2430 |
| net_avg_win | 61.4747 |
| net_avg_loss | -77.5107 |
| avg_hold_time_bars | 8.1601 |
| exposure | 0.2455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

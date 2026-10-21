# EMA Hourly Continuation — DUSK/USDT P20_55

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.7341 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -2.6310 |
| sortino_ratio | -0.8791 |
| max_drawdown | 0.7085 |
| cagr | -0.3329 |
| net_avg_win | 68.0198 |
| net_avg_loss | -82.4729 |
| avg_hold_time_bars | 8.1036 |
| exposure | 0.2026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

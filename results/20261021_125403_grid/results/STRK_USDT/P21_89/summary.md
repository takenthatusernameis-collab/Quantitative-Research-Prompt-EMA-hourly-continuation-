# EMA Hourly Continuation — STRK/USDT P21_89

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7595 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -1.9256 |
| sortino_ratio | -0.6100 |
| max_drawdown | 0.5244 |
| cagr | -0.2451 |
| net_avg_win | 67.1945 |
| net_avg_loss | -82.5727 |
| avg_hold_time_bars | 15.4422 |
| exposure | 0.3460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

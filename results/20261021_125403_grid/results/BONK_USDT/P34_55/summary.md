# EMA Hourly Continuation — BONK/USDT P34_55

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.9531 |
| net_win_rate | 0.5538 |
| gross_profit_factor | 1.2332 |
| gross_win_rate | 0.5538 |
| sharpe_ratio | -0.2248 |
| sortino_ratio | -0.0527 |
| max_drawdown | 0.2849 |
| cagr | -0.0278 |
| net_avg_win | 96.4026 |
| net_avg_loss | -125.5602 |
| avg_hold_time_bars | 5.1923 |
| exposure | 0.0614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

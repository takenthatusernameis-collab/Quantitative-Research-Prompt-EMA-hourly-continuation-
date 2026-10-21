# EMA Hourly Continuation — BONK/USDT P50_89

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7748 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.3107 |
| sortino_ratio | -0.3270 |
| max_drawdown | 0.3620 |
| cagr | -0.1402 |
| net_avg_win | 72.4111 |
| net_avg_loss | -91.0320 |
| avg_hold_time_bars | 8.1020 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

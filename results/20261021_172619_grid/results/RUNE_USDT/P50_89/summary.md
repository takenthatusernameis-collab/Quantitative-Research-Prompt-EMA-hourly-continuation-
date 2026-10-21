# EMA Hourly Continuation — RUNE/USDT P50_89

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8279 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1335 |
| gross_win_rate | 0.5382 |
| sharpe_ratio | -0.9670 |
| sortino_ratio | -0.2580 |
| max_drawdown | 0.3525 |
| cagr | -0.1125 |
| net_avg_win | 68.0678 |
| net_avg_loss | -95.8370 |
| avg_hold_time_bars | 8.5206 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

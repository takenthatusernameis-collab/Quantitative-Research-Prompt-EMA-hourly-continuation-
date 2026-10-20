# EMA Hourly Continuation — PUFFER/USDT P26_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7394 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0622 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -2.2406 |
| sortino_ratio | -0.8129 |
| max_drawdown | 0.5497 |
| cagr | -0.3183 |
| net_avg_win | 56.7863 |
| net_avg_loss | -80.6970 |
| avg_hold_time_bars | 11.3067 |
| exposure | 0.3359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

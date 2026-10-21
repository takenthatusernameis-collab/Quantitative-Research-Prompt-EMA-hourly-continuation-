# EMA Hourly Continuation — JST/USDT P26_200

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.5238 |
| gross_profit_factor | 1.0655 |
| gross_win_rate | 0.5238 |
| sharpe_ratio | -1.3676 |
| sortino_ratio | -0.3341 |
| max_drawdown | 0.3455 |
| cagr | -0.1446 |
| net_avg_win | 62.2959 |
| net_avg_loss | -91.7860 |
| avg_hold_time_bars | 38.6327 |
| exposure | 0.5140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

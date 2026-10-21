# EMA Hourly Continuation — RUNE/USDT P21_200

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.9394 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1260 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -0.2549 |
| sortino_ratio | -0.0576 |
| max_drawdown | 0.1475 |
| cagr | -0.0296 |
| net_avg_win | 86.7140 |
| net_avg_loss | -104.3467 |
| avg_hold_time_bars | 61.5020 |
| exposure | 0.6849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

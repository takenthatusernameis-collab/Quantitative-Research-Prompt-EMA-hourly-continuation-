# EMA Hourly Continuation — RUNE/USDT P26_50

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7387 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0484 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.9482 |
| sortino_ratio | -0.5573 |
| max_drawdown | 0.4753 |
| cagr | -0.2237 |
| net_avg_win | 65.8639 |
| net_avg_loss | -93.3134 |
| avg_hold_time_bars | 6.5392 |
| exposure | 0.1174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

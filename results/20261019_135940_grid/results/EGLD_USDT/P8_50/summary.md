# EMA Hourly Continuation — EGLD/USDT P8_50

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.5839 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -6.0028 |
| sortino_ratio | -2.7562 |
| max_drawdown | 0.9681 |
| cagr | -0.7414 |
| net_avg_win | 26.5419 |
| net_avg_loss | -40.6793 |
| avg_hold_time_bars | 9.2357 |
| exposure | 0.4542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

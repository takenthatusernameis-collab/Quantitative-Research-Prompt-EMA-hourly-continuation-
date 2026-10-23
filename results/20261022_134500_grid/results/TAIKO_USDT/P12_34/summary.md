# EMA Hourly Continuation — TAIKO/USDT P12_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1151 |
| net_profit_factor | 0.5481 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -8.5198 |
| sortino_ratio | -4.1771 |
| max_drawdown | 0.9934 |
| cagr | -0.8756 |
| net_avg_win | 22.9380 |
| net_avg_loss | -35.0988 |
| avg_hold_time_bars | 4.6195 |
| exposure | 0.2554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

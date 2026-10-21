# EMA Hourly Continuation — DODO/USDT P26_34

**Symbol:** DODO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.5205 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.7640 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -3.2405 |
| sortino_ratio | -0.7667 |
| max_drawdown | 0.5884 |
| cagr | -0.2967 |
| net_avg_win | 52.7978 |
| net_avg_loss | -79.6943 |
| avg_hold_time_bars | 5.3127 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

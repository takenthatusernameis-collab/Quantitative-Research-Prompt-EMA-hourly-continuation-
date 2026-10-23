# EMA Hourly Continuation — ANYONE/USDT P12_20

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1284 |
| net_profit_factor | 0.3726 |
| net_win_rate | 0.3894 |
| gross_profit_factor | 0.6495 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -11.3046 |
| sortino_ratio | -6.0354 |
| max_drawdown | 0.9988 |
| cagr | -0.9490 |
| net_avg_win | 11.8649 |
| net_avg_loss | -20.3067 |
| avg_hold_time_bars | 2.6924 |
| exposure | 0.1747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

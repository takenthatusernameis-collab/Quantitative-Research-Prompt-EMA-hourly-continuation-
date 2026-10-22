# EMA Hourly Continuation — AEVO/USDT P20_89

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.7819 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9691 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -1.8944 |
| sortino_ratio | -0.6108 |
| max_drawdown | 0.5760 |
| cagr | -0.2458 |
| net_avg_win | 72.7044 |
| net_avg_loss | -89.4238 |
| avg_hold_time_bars | 17.3398 |
| exposure | 0.4017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — OSMO/USDT P34_100

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9230 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -2.3552 |
| sortino_ratio | -0.7059 |
| max_drawdown | 0.5609 |
| cagr | -0.2770 |
| net_avg_win | 62.6639 |
| net_avg_loss | -81.7088 |
| avg_hold_time_bars | 14.6100 |
| exposure | 0.2929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

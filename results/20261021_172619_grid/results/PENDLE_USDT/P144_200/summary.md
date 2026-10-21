# EMA Hourly Continuation — PENDLE/USDT P144_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.5992 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.7684 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -2.2632 |
| sortino_ratio | -0.4980 |
| max_drawdown | 0.4365 |
| cagr | -0.2042 |
| net_avg_win | 60.9792 |
| net_avg_loss | -81.8745 |
| avg_hold_time_bars | 6.4042 |
| exposure | 0.0699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

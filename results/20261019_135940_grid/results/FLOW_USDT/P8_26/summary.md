# EMA Hourly Continuation — FLOW/USDT P8_26

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1634 |
| net_profit_factor | 0.3865 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.8187 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -11.2047 |
| sortino_ratio | -6.3942 |
| max_drawdown | 0.9997 |
| cagr | -0.9579 |
| net_avg_win | 8.8714 |
| net_avg_loss | -17.6355 |
| avg_hold_time_bars | 3.7277 |
| exposure | 0.2769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

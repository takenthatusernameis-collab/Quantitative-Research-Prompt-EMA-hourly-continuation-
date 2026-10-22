# EMA Hourly Continuation — CWEB/USDT P89_200

**Symbol:** CWEB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.5966 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -2.9681 |
| sortino_ratio | -0.6891 |
| max_drawdown | 0.6097 |
| cagr | -0.2908 |
| net_avg_win | 64.7628 |
| net_avg_loss | -98.8236 |
| avg_hold_time_bars | 20.9206 |
| exposure | 0.2634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

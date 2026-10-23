# EMA Hourly Continuation — ASTR/USDT P26_34

**Symbol:** ASTR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.2442 |
| net_win_rate | 0.3867 |
| gross_profit_factor | 0.7626 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -11.3371 |
| sortino_ratio | -5.0124 |
| max_drawdown | 0.9986 |
| cagr | -0.9264 |
| net_avg_win | 8.8388 |
| net_avg_loss | -22.8192 |
| avg_hold_time_bars | 2.8231 |
| exposure | 0.1206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

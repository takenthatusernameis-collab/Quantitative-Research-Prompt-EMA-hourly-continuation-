# EMA Hourly Continuation — CARV/USDT P26_200

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6355 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.7652 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -2.5698 |
| sortino_ratio | -0.6634 |
| max_drawdown | 0.5014 |
| cagr | -0.2636 |
| net_avg_win | 68.9241 |
| net_avg_loss | -82.9322 |
| avg_hold_time_bars | 33.4741 |
| exposure | 0.5086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

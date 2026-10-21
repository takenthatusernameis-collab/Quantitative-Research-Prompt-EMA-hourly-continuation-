# EMA Hourly Continuation — LQTY/USDT P20_34

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7112 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.2914 |
| sortino_ratio | -0.7251 |
| max_drawdown | 0.5684 |
| cagr | -0.2824 |
| net_avg_win | 56.5395 |
| net_avg_loss | -82.1603 |
| avg_hold_time_bars | 5.2428 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

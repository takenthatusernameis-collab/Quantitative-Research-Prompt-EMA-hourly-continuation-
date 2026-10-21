# EMA Hourly Continuation — SLP/USDT P21_100

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0147 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.8176 |
| sortino_ratio | -0.5933 |
| max_drawdown | 0.5516 |
| cagr | -0.2398 |
| net_avg_win | 75.8441 |
| net_avg_loss | -94.3344 |
| avg_hold_time_bars | 17.8981 |
| exposure | 0.4230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

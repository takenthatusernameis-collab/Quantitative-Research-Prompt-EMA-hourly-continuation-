# EMA Hourly Continuation — MASK/USDT P8_12

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1781 |
| net_profit_factor | 0.1647 |
| net_win_rate | 0.3431 |
| gross_profit_factor | 0.6435 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -18.7823 |
| sortino_ratio | -11.5890 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 3.2268 |
| net_avg_loss | -10.2321 |
| avg_hold_time_bars | 2.2970 |
| exposure | 0.1860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

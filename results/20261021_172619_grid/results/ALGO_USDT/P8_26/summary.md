# EMA Hourly Continuation — ALGO/USDT P8_26

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.8722 |
| net_win_rate | 0.5423 |
| gross_profit_factor | 1.1887 |
| gross_win_rate | 0.5423 |
| sharpe_ratio | -1.1302 |
| sortino_ratio | -0.4136 |
| max_drawdown | 0.4200 |
| cagr | -0.1760 |
| net_avg_win | 75.9281 |
| net_avg_loss | -103.1522 |
| avg_hold_time_bars | 6.6395 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

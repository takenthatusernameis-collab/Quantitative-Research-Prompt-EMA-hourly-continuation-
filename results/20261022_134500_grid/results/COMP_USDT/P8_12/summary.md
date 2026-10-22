# EMA Hourly Continuation — COMP/USDT P8_12

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1886 |
| net_profit_factor | 0.1469 |
| net_win_rate | 0.3547 |
| gross_profit_factor | 0.6148 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -18.6461 |
| sortino_ratio | -11.8187 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 2.5740 |
| net_avg_loss | -9.6319 |
| avg_hold_time_bars | 2.0376 |
| exposure | 0.1747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CTSI/USDT P26_89

**Symbol:** CTSI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.5912 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.9057 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -5.8321 |
| sortino_ratio | -2.2668 |
| max_drawdown | 0.9385 |
| cagr | -0.6637 |
| net_avg_win | 40.9802 |
| net_avg_loss | -52.9530 |
| avg_hold_time_bars | 9.3793 |
| exposure | 0.3249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

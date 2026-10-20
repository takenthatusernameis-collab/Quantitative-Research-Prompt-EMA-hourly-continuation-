# EMA Hourly Continuation — ARPA/USDT P34_89

**Symbol:** ARPA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5067 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.8394 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -6.6919 |
| sortino_ratio | -2.5764 |
| max_drawdown | 0.9585 |
| cagr | -0.7120 |
| net_avg_win | 31.4001 |
| net_avg_loss | -44.6899 |
| avg_hold_time_bars | 7.8112 |
| exposure | 0.2640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XLM/USDT P26_100

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0759 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.3991 |
| sortino_ratio | -0.4155 |
| max_drawdown | 0.4120 |
| cagr | -0.1736 |
| net_avg_win | 65.0608 |
| net_avg_loss | -89.1313 |
| avg_hold_time_bars | 18.2024 |
| exposure | 0.3516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

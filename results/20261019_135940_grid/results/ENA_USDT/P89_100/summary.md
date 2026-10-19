# EMA Hourly Continuation — ENA/USDT P89_100

**Symbol:** ENA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.3284 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.6881 |
| gross_win_rate | 0.4052 |
| sharpe_ratio | -8.0578 |
| sortino_ratio | -2.6921 |
| max_drawdown | 0.9707 |
| cagr | -0.7528 |
| net_avg_win | 21.9655 |
| net_avg_loss | -44.1760 |
| avg_hold_time_bars | 1.7698 |
| exposure | 0.0437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

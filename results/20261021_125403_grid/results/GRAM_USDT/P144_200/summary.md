# EMA Hourly Continuation — GRAM/USDT P144_200

**Symbol:** GRAM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 181 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8679 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.0695 |
| sortino_ratio | -0.3997 |
| max_drawdown | 0.3920 |
| cagr | -0.1671 |
| net_avg_win | 59.1327 |
| net_avg_loss | -92.2840 |
| avg_hold_time_bars | 8.2155 |
| exposure | 0.0676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

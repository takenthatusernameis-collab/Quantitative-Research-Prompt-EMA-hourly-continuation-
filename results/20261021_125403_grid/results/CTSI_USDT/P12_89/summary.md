# EMA Hourly Continuation — CTSI/USDT P12_89

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7415 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.5299 |
| sortino_ratio | -0.8602 |
| max_drawdown | 0.6336 |
| cagr | -0.3271 |
| net_avg_win | 66.2133 |
| net_avg_loss | -82.3621 |
| avg_hold_time_bars | 19.7293 |
| exposure | 0.5103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

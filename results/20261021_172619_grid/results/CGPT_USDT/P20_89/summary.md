# EMA Hourly Continuation — CGPT/USDT P20_89

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.8507 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.1539 |
| sortino_ratio | -0.3702 |
| max_drawdown | 0.3951 |
| cagr | -0.1591 |
| net_avg_win | 78.5102 |
| net_avg_loss | -97.2319 |
| avg_hold_time_bars | 15.5892 |
| exposure | 0.3536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

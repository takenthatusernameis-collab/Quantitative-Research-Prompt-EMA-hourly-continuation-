# EMA Hourly Continuation — ZBCN/USDT P50_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6539 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9467 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -3.1607 |
| sortino_ratio | -1.0732 |
| max_drawdown | 0.7387 |
| cagr | -0.4045 |
| net_avg_win | 48.5224 |
| net_avg_loss | -70.2058 |
| avg_hold_time_bars | 9.1557 |
| exposure | 0.2448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

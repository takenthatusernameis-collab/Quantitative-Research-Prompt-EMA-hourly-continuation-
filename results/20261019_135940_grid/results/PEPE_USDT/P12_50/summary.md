# EMA Hourly Continuation — PEPE/USDT P12_50

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.6786 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 1.0594 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -5.6885 |
| sortino_ratio | -2.6704 |
| max_drawdown | 0.9628 |
| cagr | -0.7244 |
| net_avg_win | 37.6413 |
| net_avg_loss | -52.0831 |
| avg_hold_time_bars | 6.4106 |
| exposure | 0.3243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

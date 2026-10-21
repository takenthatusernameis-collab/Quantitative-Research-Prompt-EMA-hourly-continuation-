# EMA Hourly Continuation — POPCAT/USDT P8_21

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.7917 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -2.1185 |
| sortino_ratio | -0.7416 |
| max_drawdown | 0.5859 |
| cagr | -0.2901 |
| net_avg_win | 77.6643 |
| net_avg_loss | -97.3344 |
| avg_hold_time_bars | 5.6654 |
| exposure | 0.1538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

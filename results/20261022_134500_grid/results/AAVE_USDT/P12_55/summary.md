# EMA Hourly Continuation — AAVE/USDT P12_55

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.5488 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -7.0158 |
| sortino_ratio | -3.1038 |
| max_drawdown | 0.9786 |
| cagr | -0.7817 |
| net_avg_win | 26.9751 |
| net_avg_loss | -38.9176 |
| avg_hold_time_bars | 8.2325 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

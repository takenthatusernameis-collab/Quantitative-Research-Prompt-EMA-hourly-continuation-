# EMA Hourly Continuation — ID/USDT P12_100

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8426 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0494 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.1499 |
| sortino_ratio | -0.3589 |
| max_drawdown | 0.3869 |
| cagr | -0.1550 |
| net_avg_win | 75.9181 |
| net_avg_loss | -94.7619 |
| avg_hold_time_bars | 26.7059 |
| exposure | 0.5753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

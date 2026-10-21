# EMA Hourly Continuation — AXS/USDT P12_100

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8898 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.0974 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -0.7605 |
| sortino_ratio | -0.2387 |
| max_drawdown | 0.2831 |
| cagr | -0.1079 |
| net_avg_win | 80.8003 |
| net_avg_loss | -100.0117 |
| avg_hold_time_bars | 25.2621 |
| exposure | 0.5453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HTX/USDT P8_50

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.2758 |
| net_win_rate | 0.3293 |
| gross_profit_factor | 0.7246 |
| gross_win_rate | 0.3861 |
| sharpe_ratio | -15.0409 |
| sortino_ratio | -7.4700 |
| max_drawdown | 1.0000 |
| cagr | -0.9823 |
| net_avg_win | 9.9443 |
| net_avg_loss | -17.7029 |
| avg_hold_time_bars | 9.5082 |
| exposure | 0.5004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — IMX/USDT P34_200

**Symbol:** IMX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 1.1547 |
| net_win_rate | 0.5749 |
| gross_profit_factor | 1.3599 |
| gross_win_rate | 0.5749 |
| sharpe_ratio | 0.7823 |
| sortino_ratio | 0.1938 |
| max_drawdown | 0.0949 |
| cagr | 0.0804 |
| net_avg_win | 97.3988 |
| net_avg_loss | -114.0799 |
| avg_hold_time_bars | 42.6899 |
| exposure | 0.5544 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

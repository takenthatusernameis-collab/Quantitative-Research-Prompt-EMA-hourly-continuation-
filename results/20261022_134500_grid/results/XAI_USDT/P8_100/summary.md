# EMA Hourly Continuation — XAI/USDT P8_100

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.6859 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9603 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.5240 |
| sortino_ratio | -1.2080 |
| max_drawdown | 0.7955 |
| cagr | -0.4428 |
| net_avg_win | 59.3837 |
| net_avg_loss | -77.0532 |
| avg_hold_time_bars | 26.0566 |
| exposure | 0.7118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

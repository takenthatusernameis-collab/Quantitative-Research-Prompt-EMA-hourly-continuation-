# EMA Hourly Continuation — SQD/USDT P34_55

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7829 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.4645 |
| sortino_ratio | -0.3851 |
| max_drawdown | 0.4078 |
| cagr | -0.1621 |
| net_avg_win | 77.6903 |
| net_avg_loss | -98.0290 |
| avg_hold_time_bars | 6.6227 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

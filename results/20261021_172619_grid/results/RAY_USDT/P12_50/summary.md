# EMA Hourly Continuation — RAY/USDT P12_50

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.8405 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0444 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.6647 |
| sortino_ratio | -0.6109 |
| max_drawdown | 0.6002 |
| cagr | -0.2473 |
| net_avg_win | 80.9677 |
| net_avg_loss | -98.7097 |
| avg_hold_time_bars | 10.0122 |
| exposure | 0.2985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

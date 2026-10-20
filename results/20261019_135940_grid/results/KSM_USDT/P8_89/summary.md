# EMA Hourly Continuation — KSM/USDT P8_89

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6156 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -4.4062 |
| sortino_ratio | -1.6007 |
| max_drawdown | 0.8584 |
| cagr | -0.5343 |
| net_avg_win | 44.5049 |
| net_avg_loss | -61.6556 |
| avg_hold_time_bars | 21.9145 |
| exposure | 0.6644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XNO/USDT P20_55

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1127 |
| net_profit_factor | 0.4488 |
| net_win_rate | 0.3913 |
| gross_profit_factor | 0.7781 |
| gross_win_rate | 0.4046 |
| sharpe_ratio | -9.8728 |
| sortino_ratio | -4.6959 |
| max_drawdown | 0.9971 |
| cagr | -0.8998 |
| net_avg_win | 18.4065 |
| net_avg_loss | -26.3649 |
| avg_hold_time_bars | 4.4756 |
| exposure | 0.2293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

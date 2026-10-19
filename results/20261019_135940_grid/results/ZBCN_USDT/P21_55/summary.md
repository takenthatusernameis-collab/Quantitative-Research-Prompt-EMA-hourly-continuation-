# EMA Hourly Continuation — ZBCN/USDT P21_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.5694 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -6.1783 |
| sortino_ratio | -2.8434 |
| max_drawdown | 0.9689 |
| cagr | -0.7496 |
| net_avg_win | 26.0521 |
| net_avg_loss | -39.5481 |
| avg_hold_time_bars | 4.1020 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CRV/USDT P21_200

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9984 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.3537 |
| sortino_ratio | -0.6681 |
| max_drawdown | 0.5760 |
| cagr | -0.2737 |
| net_avg_win | 70.7950 |
| net_avg_loss | -95.0679 |
| avg_hold_time_bars | 32.6658 |
| exposure | 0.6043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

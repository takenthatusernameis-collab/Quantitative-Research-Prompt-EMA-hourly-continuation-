# EMA Hourly Continuation — ARPA/USDT P55_89

**Symbol:** ARPA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.3910 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.7587 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -8.0061 |
| sortino_ratio | -3.0577 |
| max_drawdown | 0.9784 |
| cagr | -0.7799 |
| net_avg_win | 21.2891 |
| net_avg_loss | -36.7523 |
| avg_hold_time_bars | 4.5751 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

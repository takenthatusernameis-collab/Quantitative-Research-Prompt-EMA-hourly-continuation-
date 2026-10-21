# EMA Hourly Continuation — SYN/USDT P12_89

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.8901 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0603 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -0.7844 |
| sortino_ratio | -0.2585 |
| max_drawdown | 0.3214 |
| cagr | -0.1170 |
| net_avg_win | 79.9598 |
| net_avg_loss | -96.1952 |
| avg_hold_time_bars | 21.9886 |
| exposure | 0.5257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

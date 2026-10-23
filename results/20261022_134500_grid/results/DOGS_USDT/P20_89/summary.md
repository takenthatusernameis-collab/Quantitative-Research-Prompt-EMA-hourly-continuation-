# EMA Hourly Continuation — DOGS/USDT P20_89

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6730 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -3.0839 |
| sortino_ratio | -1.2069 |
| max_drawdown | 0.7053 |
| cagr | -0.4314 |
| net_avg_win | 44.3874 |
| net_avg_loss | -66.3650 |
| avg_hold_time_bars | 11.2277 |
| exposure | 0.3872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

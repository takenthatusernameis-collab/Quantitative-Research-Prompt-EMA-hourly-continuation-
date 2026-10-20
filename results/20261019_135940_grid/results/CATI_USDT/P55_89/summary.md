# EMA Hourly Continuation — CATI/USDT P55_89

**Symbol:** CATI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.4614 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -7.3285 |
| sortino_ratio | -2.8358 |
| max_drawdown | 0.9505 |
| cagr | -0.7582 |
| net_avg_win | 29.4236 |
| net_avg_loss | -50.0028 |
| avg_hold_time_bars | 4.6083 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

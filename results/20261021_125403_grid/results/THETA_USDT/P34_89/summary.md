# EMA Hourly Continuation — THETA/USDT P34_89

**Symbol:** THETA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7719 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9935 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.6743 |
| sortino_ratio | -0.5005 |
| max_drawdown | 0.4611 |
| cagr | -0.2054 |
| net_avg_win | 68.4110 |
| net_avg_loss | -88.2167 |
| avg_hold_time_bars | 9.8368 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

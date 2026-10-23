# EMA Hourly Continuation — TURBO/USDT P55_89

**Symbol:** TURBO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -4.6544 |
| sortino_ratio | -1.7409 |
| max_drawdown | 0.8331 |
| cagr | -0.5662 |
| net_avg_win | 46.0259 |
| net_avg_loss | -70.1697 |
| avg_hold_time_bars | 3.9708 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

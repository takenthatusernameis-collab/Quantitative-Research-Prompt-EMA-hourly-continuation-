# EMA Hourly Continuation — ALEX/USDT P50_89

**Symbol:** ALEX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.4493 |
| net_win_rate | 0.3641 |
| gross_profit_factor | 0.7854 |
| gross_win_rate | 0.3822 |
| sharpe_ratio | -7.2762 |
| sortino_ratio | -2.4097 |
| max_drawdown | 0.9502 |
| cagr | -0.6948 |
| net_avg_win | 38.5230 |
| net_avg_loss | -49.1034 |
| avg_hold_time_bars | 8.2210 |
| exposure | 0.2063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

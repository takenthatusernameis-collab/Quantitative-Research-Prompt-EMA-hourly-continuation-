# EMA Hourly Continuation — WIN/USDT P8_89

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7983 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0523 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.5796 |
| sortino_ratio | -0.5084 |
| max_drawdown | 0.4809 |
| cagr | -0.2103 |
| net_avg_win | 68.6267 |
| net_avg_loss | -90.5259 |
| avg_hold_time_bars | 27.2724 |
| exposure | 0.6235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

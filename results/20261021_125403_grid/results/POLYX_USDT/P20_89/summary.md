# EMA Hourly Continuation — POLYX/USDT P20_89

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7983 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0332 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.7911 |
| sortino_ratio | -0.5965 |
| max_drawdown | 0.5673 |
| cagr | -0.2407 |
| net_avg_win | 72.0858 |
| net_avg_loss | -92.6720 |
| avg_hold_time_bars | 15.2810 |
| exposure | 0.3758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

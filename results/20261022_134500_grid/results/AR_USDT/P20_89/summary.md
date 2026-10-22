# EMA Hourly Continuation — AR/USDT P20_89

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5931 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.5053 |
| sortino_ratio | -1.6959 |
| max_drawdown | 0.8771 |
| cagr | -0.5608 |
| net_avg_win | 38.1050 |
| net_avg_loss | -54.6061 |
| avg_hold_time_bars | 11.0619 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

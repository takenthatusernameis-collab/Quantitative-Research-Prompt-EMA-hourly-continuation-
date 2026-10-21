# EMA Hourly Continuation — SUN/USDT P55_89

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.3482 |
| net_win_rate | 0.3718 |
| gross_profit_factor | 0.6959 |
| gross_win_rate | 0.3972 |
| sharpe_ratio | -6.6917 |
| sortino_ratio | -1.8244 |
| max_drawdown | 0.8967 |
| cagr | -0.5920 |
| net_avg_win | 36.2572 |
| net_avg_loss | -61.6314 |
| avg_hold_time_bars | 7.7831 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

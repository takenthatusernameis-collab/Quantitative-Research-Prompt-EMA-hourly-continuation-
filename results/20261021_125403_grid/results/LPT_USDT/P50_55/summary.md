# EMA Hourly Continuation — LPT/USDT P50_55

**Symbol:** LPT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.6059 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -2.1027 |
| sortino_ratio | -0.3997 |
| max_drawdown | 0.3849 |
| cagr | -0.1674 |
| net_avg_win | 68.3065 |
| net_avg_loss | -100.6057 |
| avg_hold_time_bars | 5.2045 |
| exposure | 0.0416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

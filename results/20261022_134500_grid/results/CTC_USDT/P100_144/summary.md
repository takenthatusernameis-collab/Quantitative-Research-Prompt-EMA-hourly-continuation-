# EMA Hourly Continuation — CTC/USDT P100_144

**Symbol:** CTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.4085 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.9170 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -6.5816 |
| sortino_ratio | -2.0951 |
| max_drawdown | 0.9338 |
| cagr | -0.6596 |
| net_avg_win | 29.2989 |
| net_avg_loss | -54.4059 |
| avg_hold_time_bars | 3.9686 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

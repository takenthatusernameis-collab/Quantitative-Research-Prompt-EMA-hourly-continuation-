# EMA Hourly Continuation — JASMY/USDT P55_144

**Symbol:** JASMY/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7961 |
| net_win_rate | 0.5473 |
| gross_profit_factor | 1.1871 |
| gross_win_rate | 0.5514 |
| sharpe_ratio | -1.3965 |
| sortino_ratio | -0.4364 |
| max_drawdown | 0.4560 |
| cagr | -0.1894 |
| net_avg_win | 60.1769 |
| net_avg_loss | -91.3896 |
| avg_hold_time_bars | 10.9115 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

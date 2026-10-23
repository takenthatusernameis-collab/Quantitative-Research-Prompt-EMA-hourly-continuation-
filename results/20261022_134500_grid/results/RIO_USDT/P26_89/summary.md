# EMA Hourly Continuation — RIO/USDT P26_89

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 830 |
| net_profit_factor | 0.5384 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.7440 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -6.0139 |
| sortino_ratio | -2.4433 |
| max_drawdown | 0.9488 |
| cagr | -0.6909 |
| net_avg_win | 31.8000 |
| net_avg_loss | -42.4327 |
| avg_hold_time_bars | 7.6627 |
| exposure | 0.2920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

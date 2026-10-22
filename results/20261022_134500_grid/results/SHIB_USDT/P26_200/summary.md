# EMA Hourly Continuation — SHIB/USDT P26_200

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6826 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0395 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.7010 |
| sortino_ratio | -0.7795 |
| max_drawdown | 0.6256 |
| cagr | -0.3160 |
| net_avg_win | 62.0591 |
| net_avg_loss | -91.3475 |
| avg_hold_time_bars | 27.1765 |
| exposure | 0.5250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — NYM/USDT P100_200

**Symbol:** NYM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.2612 |
| net_win_rate | 0.3489 |
| gross_profit_factor | 0.5665 |
| gross_win_rate | 0.3612 |
| sharpe_ratio | -7.5443 |
| sortino_ratio | -2.1695 |
| max_drawdown | 0.9414 |
| cagr | -0.6770 |
| net_avg_win | 23.4408 |
| net_avg_loss | -48.0866 |
| avg_hold_time_bars | 10.2948 |
| exposure | 0.1905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

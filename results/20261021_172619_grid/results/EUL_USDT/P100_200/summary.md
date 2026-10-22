# EMA Hourly Continuation — EUL/USDT P100_200

**Symbol:** EUL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8040 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -2.0780 |
| sortino_ratio | -0.4642 |
| max_drawdown | 0.4201 |
| cagr | -0.1916 |
| net_avg_win | 64.0524 |
| net_avg_loss | -83.1780 |
| avg_hold_time_bars | 11.4435 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

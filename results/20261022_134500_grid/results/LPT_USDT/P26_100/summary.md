# EMA Hourly Continuation — LPT/USDT P26_100

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.5374 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.8159 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -5.2741 |
| sortino_ratio | -1.9709 |
| max_drawdown | 0.9113 |
| cagr | -0.6130 |
| net_avg_win | 33.7983 |
| net_avg_loss | -49.1815 |
| avg_hold_time_bars | 10.3615 |
| exposure | 0.3349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

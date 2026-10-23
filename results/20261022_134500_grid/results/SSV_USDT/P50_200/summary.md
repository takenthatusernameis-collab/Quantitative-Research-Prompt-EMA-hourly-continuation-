# EMA Hourly Continuation — SSV/USDT P50_200

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5981 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8350 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -3.3422 |
| sortino_ratio | -0.9731 |
| max_drawdown | 0.7017 |
| cagr | -0.3729 |
| net_avg_win | 51.4790 |
| net_avg_loss | -72.9405 |
| avg_hold_time_bars | 20.3073 |
| exposure | 0.4007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

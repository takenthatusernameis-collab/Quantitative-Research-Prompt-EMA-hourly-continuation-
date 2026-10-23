# EMA Hourly Continuation — KNC/USDT P26_100

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.6128 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.9903 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -4.3832 |
| sortino_ratio | -1.4911 |
| max_drawdown | 0.8455 |
| cagr | -0.5108 |
| net_avg_win | 48.8836 |
| net_avg_loss | -69.0330 |
| avg_hold_time_bars | 14.4502 |
| exposure | 0.3823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

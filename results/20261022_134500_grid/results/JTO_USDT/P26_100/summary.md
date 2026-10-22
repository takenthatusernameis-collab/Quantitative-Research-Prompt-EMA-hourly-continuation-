# EMA Hourly Continuation — JTO/USDT P26_100

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -3.2073 |
| sortino_ratio | -1.1400 |
| max_drawdown | 0.7566 |
| cagr | -0.4121 |
| net_avg_win | 52.9319 |
| net_avg_loss | -69.7465 |
| avg_hold_time_bars | 11.9745 |
| exposure | 0.3418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

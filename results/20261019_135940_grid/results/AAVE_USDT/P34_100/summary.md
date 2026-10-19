# EMA Hourly Continuation — AAVE/USDT P34_100

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.5345 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -5.0020 |
| sortino_ratio | -1.7641 |
| max_drawdown | 0.8964 |
| cagr | -0.5790 |
| net_avg_win | 34.8494 |
| net_avg_loss | -56.3228 |
| avg_hold_time_bars | 9.6111 |
| exposure | 0.2752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

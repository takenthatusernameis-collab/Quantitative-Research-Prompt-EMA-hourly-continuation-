# EMA Hourly Continuation — TRX/USDT P26_55

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.4025 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9505 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -4.9450 |
| sortino_ratio | -1.3575 |
| max_drawdown | 0.7947 |
| cagr | -0.4598 |
| net_avg_win | 31.5499 |
| net_avg_loss | -72.7632 |
| avg_hold_time_bars | 7.5989 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

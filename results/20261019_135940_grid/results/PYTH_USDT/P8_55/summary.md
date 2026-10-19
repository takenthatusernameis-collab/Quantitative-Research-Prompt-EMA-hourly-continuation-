# EMA Hourly Continuation — PYTH/USDT P8_55

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9938 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -4.9059 |
| sortino_ratio | -2.2336 |
| max_drawdown | 0.9346 |
| cagr | -0.6593 |
| net_avg_win | 37.0903 |
| net_avg_loss | -50.6094 |
| avg_hold_time_bars | 9.8788 |
| exposure | 0.4742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

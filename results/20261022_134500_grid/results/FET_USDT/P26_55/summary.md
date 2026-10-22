# EMA Hourly Continuation — FET/USDT P26_55

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.4671 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8039 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -6.6721 |
| sortino_ratio | -2.8442 |
| max_drawdown | 0.9712 |
| cagr | -0.7532 |
| net_avg_win | 20.1559 |
| net_avg_loss | -36.4160 |
| avg_hold_time_bars | 3.9176 |
| exposure | 0.1642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

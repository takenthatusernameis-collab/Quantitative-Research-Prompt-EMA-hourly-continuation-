# EMA Hourly Continuation — W/USDT P21_34

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.0358 |
| sortino_ratio | -0.5421 |
| max_drawdown | 0.5080 |
| cagr | -0.2202 |
| net_avg_win | 71.9508 |
| net_avg_loss | -94.0067 |
| avg_hold_time_bars | 5.1763 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

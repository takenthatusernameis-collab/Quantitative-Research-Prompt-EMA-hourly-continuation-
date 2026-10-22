# EMA Hourly Continuation — XEC/USDT P100_200

**Symbol:** XEC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4383 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.7743 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -5.2520 |
| sortino_ratio | -1.5105 |
| max_drawdown | 0.8520 |
| cagr | -0.5245 |
| net_avg_win | 37.7558 |
| net_avg_loss | -62.2894 |
| avg_hold_time_bars | 8.6091 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

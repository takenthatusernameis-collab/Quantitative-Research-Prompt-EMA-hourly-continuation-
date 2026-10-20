# EMA Hourly Continuation — MLK/USDT P12_200

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.4056 |
| net_win_rate | 0.3431 |
| gross_profit_factor | 0.5940 |
| gross_win_rate | 0.3475 |
| sharpe_ratio | -8.1170 |
| sortino_ratio | -2.9806 |
| max_drawdown | 0.9749 |
| cagr | -0.7670 |
| net_avg_win | 28.4237 |
| net_avg_loss | -36.6015 |
| avg_hold_time_bars | 21.0499 |
| exposure | 0.6497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

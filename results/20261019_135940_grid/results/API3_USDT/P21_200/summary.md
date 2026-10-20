# EMA Hourly Continuation — API3/USDT P21_200

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.6631 |
| sortino_ratio | -0.7555 |
| max_drawdown | 0.6194 |
| cagr | -0.3043 |
| net_avg_win | 60.9993 |
| net_avg_loss | -83.0367 |
| avg_hold_time_bars | 33.0170 |
| exposure | 0.6183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

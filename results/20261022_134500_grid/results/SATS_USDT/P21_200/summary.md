# EMA Hourly Continuation — SATS/USDT P21_200

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.8061 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -3.2881 |
| sortino_ratio | -0.9335 |
| max_drawdown | 0.6853 |
| cagr | -0.3544 |
| net_avg_win | 52.2628 |
| net_avg_loss | -70.0413 |
| avg_hold_time_bars | 31.3113 |
| exposure | 0.5781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

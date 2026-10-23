# EMA Hourly Continuation — AGLD/USDT P21_100

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6374 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -4.0429 |
| sortino_ratio | -1.4413 |
| max_drawdown | 0.8280 |
| cagr | -0.4922 |
| net_avg_win | 49.4731 |
| net_avg_loss | -64.5336 |
| avg_hold_time_bars | 14.9844 |
| exposure | 0.4347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

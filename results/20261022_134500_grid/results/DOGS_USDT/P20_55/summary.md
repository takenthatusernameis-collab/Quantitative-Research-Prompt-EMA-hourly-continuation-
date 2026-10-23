# EMA Hourly Continuation — DOGS/USDT P20_55

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 882 |
| net_profit_factor | 0.4840 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.7585 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -7.0384 |
| sortino_ratio | -3.1703 |
| max_drawdown | 0.9637 |
| cagr | -0.7858 |
| net_avg_win | 23.1807 |
| net_avg_loss | -37.9618 |
| avg_hold_time_bars | 5.0408 |
| exposure | 0.2359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

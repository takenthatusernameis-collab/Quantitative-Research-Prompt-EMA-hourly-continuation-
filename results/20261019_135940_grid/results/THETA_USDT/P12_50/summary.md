# EMA Hourly Continuation — THETA/USDT P12_50

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.5568 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -6.5213 |
| sortino_ratio | -2.8924 |
| max_drawdown | 0.9721 |
| cagr | -0.7540 |
| net_avg_win | 27.0889 |
| net_avg_loss | -40.2473 |
| avg_hold_time_bars | 7.8622 |
| exposure | 0.3552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

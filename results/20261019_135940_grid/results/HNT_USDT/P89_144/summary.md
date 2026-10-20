# EMA Hourly Continuation — HNT/USDT P89_144

**Symbol:** HNT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.4853 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -5.2174 |
| sortino_ratio | -1.7313 |
| max_drawdown | 0.8829 |
| cagr | -0.5672 |
| net_avg_win | 34.4952 |
| net_avg_loss | -54.1522 |
| avg_hold_time_bars | 6.1694 |
| exposure | 0.1556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

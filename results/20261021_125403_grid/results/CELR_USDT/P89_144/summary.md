# EMA Hourly Continuation — CELR/USDT P89_144

**Symbol:** CELR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6767 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9012 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.2512 |
| sortino_ratio | -0.5803 |
| max_drawdown | 0.5089 |
| cagr | -0.2342 |
| net_avg_win | 66.1704 |
| net_avg_loss | -88.1132 |
| avg_hold_time_bars | 7.4801 |
| exposure | 0.1107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

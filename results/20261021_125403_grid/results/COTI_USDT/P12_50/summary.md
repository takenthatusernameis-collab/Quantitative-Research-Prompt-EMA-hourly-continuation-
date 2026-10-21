# EMA Hourly Continuation — COTI/USDT P12_50

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7921 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.9585 |
| sortino_ratio | -0.7254 |
| max_drawdown | 0.6095 |
| cagr | -0.2842 |
| net_avg_win | 65.2050 |
| net_avg_loss | -80.8564 |
| avg_hold_time_bars | 9.5075 |
| exposure | 0.2895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

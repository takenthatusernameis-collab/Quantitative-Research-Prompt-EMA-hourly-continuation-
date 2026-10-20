# EMA Hourly Continuation — WOO/USDT P50_55

**Symbol:** WOO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.2568 |
| net_win_rate | 0.3782 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -10.6072 |
| sortino_ratio | -4.2635 |
| max_drawdown | 0.9964 |
| cagr | -0.8932 |
| net_avg_win | 11.7882 |
| net_avg_loss | -27.9287 |
| avg_hold_time_bars | 2.2953 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

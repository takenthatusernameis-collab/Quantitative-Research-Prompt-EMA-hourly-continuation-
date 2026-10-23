# EMA Hourly Continuation — LSK/USDT P8_12

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1397 |
| net_profit_factor | 0.2794 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.9965 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -13.6291 |
| sortino_ratio | -7.3039 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 7.0893 |
| net_avg_loss | -16.3261 |
| avg_hold_time_bars | 3.0229 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

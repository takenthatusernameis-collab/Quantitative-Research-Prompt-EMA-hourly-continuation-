# EMA Hourly Continuation — SATS/USDT P12_55

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.6503 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9568 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -4.2431 |
| sortino_ratio | -1.8108 |
| max_drawdown | 0.8835 |
| cagr | -0.5732 |
| net_avg_win | 37.9291 |
| net_avg_loss | -52.6171 |
| avg_hold_time_bars | 9.1544 |
| exposure | 0.3782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

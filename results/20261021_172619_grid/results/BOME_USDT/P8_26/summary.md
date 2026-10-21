# EMA Hourly Continuation — BOME/USDT P8_26

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.8381 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0525 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -1.3042 |
| sortino_ratio | -0.4797 |
| max_drawdown | 0.4806 |
| cagr | -0.2005 |
| net_avg_win | 65.8125 |
| net_avg_loss | -84.2631 |
| avg_hold_time_bars | 6.3185 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

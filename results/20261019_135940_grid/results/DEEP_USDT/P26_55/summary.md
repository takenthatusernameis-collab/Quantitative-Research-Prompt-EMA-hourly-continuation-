# EMA Hourly Continuation — DEEP/USDT P26_55

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6401 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9840 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -4.5065 |
| sortino_ratio | -1.8127 |
| max_drawdown | 0.8401 |
| cagr | -0.5784 |
| net_avg_win | 47.0152 |
| net_avg_loss | -68.2030 |
| avg_hold_time_bars | 4.8873 |
| exposure | 0.1793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

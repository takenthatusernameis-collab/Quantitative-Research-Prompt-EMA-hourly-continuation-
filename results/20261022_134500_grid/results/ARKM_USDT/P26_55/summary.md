# EMA Hourly Continuation — ARKM/USDT P26_55

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.5767 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -6.1230 |
| sortino_ratio | -2.6307 |
| max_drawdown | 0.9626 |
| cagr | -0.7193 |
| net_avg_win | 30.4487 |
| net_avg_loss | -45.3929 |
| avg_hold_time_bars | 4.1961 |
| exposure | 0.1770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

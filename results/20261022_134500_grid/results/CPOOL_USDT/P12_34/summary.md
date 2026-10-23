# EMA Hourly Continuation — CPOOL/USDT P12_34

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1255 |
| net_profit_factor | 0.6533 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.9679 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -6.4133 |
| sortino_ratio | -3.1676 |
| max_drawdown | 0.9805 |
| cagr | -0.7910 |
| net_avg_win | 31.1489 |
| net_avg_loss | -42.7114 |
| avg_hold_time_bars | 4.0972 |
| exposure | 0.2337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

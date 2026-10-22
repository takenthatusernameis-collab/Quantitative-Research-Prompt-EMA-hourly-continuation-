# EMA Hourly Continuation — KMNO/USDT P26_34

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 882 |
| net_profit_factor | 0.3960 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -9.7813 |
| sortino_ratio | -4.1929 |
| max_drawdown | 0.9947 |
| cagr | -0.8798 |
| net_avg_win | 18.0155 |
| net_avg_loss | -31.6701 |
| avg_hold_time_bars | 2.5624 |
| exposure | 0.1043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

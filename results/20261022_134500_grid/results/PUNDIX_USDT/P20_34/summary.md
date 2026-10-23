# EMA Hourly Continuation — PUNDIX/USDT P20_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1134 |
| net_profit_factor | 0.2631 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.6480 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -11.3818 |
| sortino_ratio | -5.4659 |
| max_drawdown | 0.9991 |
| cagr | -0.9377 |
| net_avg_win | 7.8223 |
| net_avg_loss | -19.9964 |
| avg_hold_time_bars | 3.5600 |
| exposure | 0.1835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

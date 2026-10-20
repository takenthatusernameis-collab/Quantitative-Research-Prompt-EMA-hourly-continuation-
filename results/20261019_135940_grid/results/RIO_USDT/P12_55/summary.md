# EMA Hourly Continuation — RIO/USDT P12_55

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.6149 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -6.8932 |
| sortino_ratio | -3.3139 |
| max_drawdown | 0.9825 |
| cagr | -0.8036 |
| net_avg_win | 30.6444 |
| net_avg_loss | -38.3111 |
| avg_hold_time_bars | 6.6885 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

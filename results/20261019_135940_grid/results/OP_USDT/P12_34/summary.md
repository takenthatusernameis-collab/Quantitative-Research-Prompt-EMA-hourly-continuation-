# EMA Hourly Continuation — OP/USDT P12_34

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1251 |
| net_profit_factor | 0.4068 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -8.8391 |
| sortino_ratio | -4.3830 |
| max_drawdown | 0.9959 |
| cagr | -0.8876 |
| net_avg_win | 12.3951 |
| net_avg_loss | -23.9834 |
| avg_hold_time_bars | 4.2342 |
| exposure | 0.2408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PUNDIX/USDT P21_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.0001 |
| sortino_ratio | -1.2251 |
| max_drawdown | 0.7626 |
| cagr | -0.4304 |
| net_avg_win | 42.6937 |
| net_avg_loss | -69.1315 |
| avg_hold_time_bars | 5.9692 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

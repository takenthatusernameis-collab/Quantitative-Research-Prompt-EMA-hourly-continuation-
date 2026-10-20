# EMA Hourly Continuation — PUNDIX/USDT P21_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1110 |
| net_profit_factor | 0.2500 |
| net_win_rate | 0.3982 |
| gross_profit_factor | 0.6282 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -11.5497 |
| sortino_ratio | -5.5049 |
| max_drawdown | 0.9991 |
| cagr | -0.9391 |
| net_avg_win | 7.5350 |
| net_avg_loss | -19.9426 |
| avg_hold_time_bars | 3.4658 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TNSR/USDT P12_20

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6430 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -3.0686 |
| sortino_ratio | -0.8959 |
| max_drawdown | 0.6591 |
| cagr | -0.3374 |
| net_avg_win | 59.0502 |
| net_avg_loss | -81.4927 |
| avg_hold_time_bars | 4.2697 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TNSR/USDT P12_20

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1452 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.9737 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -11.1506 |
| sortino_ratio | -6.0000 |
| max_drawdown | 0.9995 |
| cagr | -0.9504 |
| net_avg_win | 15.4454 |
| net_avg_loss | -23.3364 |
| avg_hold_time_bars | 2.3705 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

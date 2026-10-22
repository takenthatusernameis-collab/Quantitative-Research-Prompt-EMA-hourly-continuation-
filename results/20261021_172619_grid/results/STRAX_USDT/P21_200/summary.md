# EMA Hourly Continuation — STRAX/USDT P21_200

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.7266 |
| gross_win_rate | 0.4220 |
| sharpe_ratio | -3.8002 |
| sortino_ratio | -1.1476 |
| max_drawdown | 0.7351 |
| cagr | -0.4126 |
| net_avg_win | 50.2299 |
| net_avg_loss | -64.6193 |
| avg_hold_time_bars | 25.6286 |
| exposure | 0.5331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

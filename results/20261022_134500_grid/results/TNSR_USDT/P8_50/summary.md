# EMA Hourly Continuation — TNSR/USDT P8_50

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.6999 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 1.0253 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -4.6856 |
| sortino_ratio | -2.1292 |
| max_drawdown | 0.9256 |
| cagr | -0.6400 |
| net_avg_win | 42.6646 |
| net_avg_loss | -56.4875 |
| avg_hold_time_bars | 9.9095 |
| exposure | 0.4709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

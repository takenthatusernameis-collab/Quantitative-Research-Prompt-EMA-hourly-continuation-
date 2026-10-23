# EMA Hourly Continuation — TRADE/USDT P50_144

**Symbol:** TRADE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7462 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -3.8782 |
| sortino_ratio | -1.1072 |
| max_drawdown | 0.7465 |
| cagr | -0.4108 |
| net_avg_win | 51.6328 |
| net_avg_loss | -69.1443 |
| avg_hold_time_bars | 12.8350 |
| exposure | 0.2404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

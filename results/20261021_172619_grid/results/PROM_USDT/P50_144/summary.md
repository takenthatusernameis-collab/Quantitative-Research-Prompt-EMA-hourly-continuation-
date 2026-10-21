# EMA Hourly Continuation — PROM/USDT P50_144

**Symbol:** PROM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5766 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -3.3137 |
| sortino_ratio | -0.9400 |
| max_drawdown | 0.6820 |
| cagr | -0.3544 |
| net_avg_win | 51.0193 |
| net_avg_loss | -70.3088 |
| avg_hold_time_bars | 14.8930 |
| exposure | 0.2721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ELON/USDT P50_200

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.5778 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.7224 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -2.7870 |
| sortino_ratio | -0.6745 |
| max_drawdown | 0.5485 |
| cagr | -0.2666 |
| net_avg_win | 59.2308 |
| net_avg_loss | -76.2720 |
| avg_hold_time_bars | 27.7850 |
| exposure | 0.3700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

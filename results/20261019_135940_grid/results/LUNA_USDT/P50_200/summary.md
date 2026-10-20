# EMA Hourly Continuation — LUNA/USDT P50_200

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.5499 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8713 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -3.8365 |
| sortino_ratio | -1.1407 |
| max_drawdown | 0.7429 |
| cagr | -0.4177 |
| net_avg_win | 44.4901 |
| net_avg_loss | -68.7701 |
| avg_hold_time_bars | 19.0901 |
| exposure | 0.3853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

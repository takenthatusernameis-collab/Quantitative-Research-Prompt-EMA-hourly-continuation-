# EMA Hourly Continuation — BONK/USDT P50_200

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8623 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -2.7752 |
| sortino_ratio | -0.7220 |
| max_drawdown | 0.6304 |
| cagr | -0.2973 |
| net_avg_win | 60.0425 |
| net_avg_loss | -82.5579 |
| avg_hold_time_bars | 25.9060 |
| exposure | 0.4133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DODO/USDT P50_200

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -2.3336 |
| sortino_ratio | -0.6196 |
| max_drawdown | 0.5262 |
| cagr | -0.2481 |
| net_avg_win | 69.3710 |
| net_avg_loss | -84.0853 |
| avg_hold_time_bars | 21.9773 |
| exposure | 0.3511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

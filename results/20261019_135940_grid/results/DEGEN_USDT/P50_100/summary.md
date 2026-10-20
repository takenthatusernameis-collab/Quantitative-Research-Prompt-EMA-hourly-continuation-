# EMA Hourly Continuation — DEGEN/USDT P50_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.5491 |
| sortino_ratio | -1.2060 |
| max_drawdown | 0.7678 |
| cagr | -0.4352 |
| net_avg_win | 52.4764 |
| net_avg_loss | -71.9295 |
| avg_hold_time_bars | 7.0415 |
| exposure | 0.1853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

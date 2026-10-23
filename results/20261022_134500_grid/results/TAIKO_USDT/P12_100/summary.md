# EMA Hourly Continuation — TAIKO/USDT P12_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -3.2535 |
| sortino_ratio | -1.1628 |
| max_drawdown | 0.7597 |
| cagr | -0.4236 |
| net_avg_win | 46.9632 |
| net_avg_loss | -68.6125 |
| avg_hold_time_bars | 20.0017 |
| exposure | 0.5813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

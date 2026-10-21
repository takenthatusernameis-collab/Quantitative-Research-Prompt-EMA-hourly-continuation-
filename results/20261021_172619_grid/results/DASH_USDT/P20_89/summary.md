# EMA Hourly Continuation — DASH/USDT P20_89

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.0731 |
| sortino_ratio | -0.6409 |
| max_drawdown | 0.5826 |
| cagr | -0.2544 |
| net_avg_win | 65.8857 |
| net_avg_loss | -84.3264 |
| avg_hold_time_bars | 16.7671 |
| exposure | 0.3567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

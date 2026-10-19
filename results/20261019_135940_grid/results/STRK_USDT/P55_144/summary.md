# EMA Hourly Continuation — STRK/USDT P55_144

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9448 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -3.0874 |
| sortino_ratio | -0.9936 |
| max_drawdown | 0.7174 |
| cagr | -0.3771 |
| net_avg_win | 53.0645 |
| net_avg_loss | -74.6919 |
| avg_hold_time_bars | 9.6108 |
| exposure | 0.2267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

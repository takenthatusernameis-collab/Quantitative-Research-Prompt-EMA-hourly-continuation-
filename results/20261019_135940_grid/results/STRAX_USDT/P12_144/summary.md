# EMA Hourly Continuation — STRAX/USDT P12_144

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.5860 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8674 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -5.2022 |
| sortino_ratio | -1.9651 |
| max_drawdown | 0.9078 |
| cagr | -0.6123 |
| net_avg_win | 40.3348 |
| net_avg_loss | -53.9103 |
| avg_hold_time_bars | 17.9848 |
| exposure | 0.5953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

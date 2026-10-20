# EMA Hourly Continuation — LQTY/USDT P12_55

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8717 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -5.2405 |
| sortino_ratio | -2.2526 |
| max_drawdown | 0.9371 |
| cagr | -0.6627 |
| net_avg_win | 24.5266 |
| net_avg_loss | -40.3115 |
| avg_hold_time_bars | 10.0170 |
| exposure | 0.4274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

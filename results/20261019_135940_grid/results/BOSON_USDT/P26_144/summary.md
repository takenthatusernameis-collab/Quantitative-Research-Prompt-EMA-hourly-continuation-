# EMA Hourly Continuation — BOSON/USDT P26_144

**Symbol:** BOSON/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7286 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.5750 |
| sortino_ratio | -0.8407 |
| max_drawdown | 0.6380 |
| cagr | -0.3297 |
| net_avg_win | 65.7176 |
| net_avg_loss | -83.1299 |
| avg_hold_time_bars | 17.2704 |
| exposure | 0.4239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

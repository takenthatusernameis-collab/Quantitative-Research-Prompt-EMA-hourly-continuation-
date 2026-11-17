# EMA Hourly Continuation — NUM/USDT P26_144

**Symbol:** NUM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.5445 |
| net_win_rate | 0.4004 |
| gross_profit_factor | 0.7311 |
| gross_win_rate | 0.4045 |
| sharpe_ratio | -4.6138 |
| sortino_ratio | -1.4408 |
| max_drawdown | 0.8287 |
| cagr | -0.4915 |
| net_avg_win | 49.5763 |
| net_avg_loss | -60.8018 |
| avg_hold_time_bars | 22.0793 |
| exposure | 0.4938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

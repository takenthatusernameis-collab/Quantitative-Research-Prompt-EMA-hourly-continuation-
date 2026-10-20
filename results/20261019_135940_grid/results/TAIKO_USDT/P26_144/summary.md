# EMA Hourly Continuation — TAIKO/USDT P26_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.5828 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.6804 |
| sortino_ratio | -1.0845 |
| max_drawdown | 0.7288 |
| cagr | -0.4129 |
| net_avg_win | 51.7022 |
| net_avg_loss | -74.4991 |
| avg_hold_time_bars | 24.2376 |
| exposure | 0.4948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

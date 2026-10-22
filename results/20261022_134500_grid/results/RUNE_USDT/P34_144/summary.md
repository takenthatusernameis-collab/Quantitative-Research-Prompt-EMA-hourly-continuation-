# EMA Hourly Continuation — RUNE/USDT P34_144

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7532 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0907 |
| gross_win_rate | 0.5308 |
| sharpe_ratio | -1.6868 |
| sortino_ratio | -0.5017 |
| max_drawdown | 0.4955 |
| cagr | -0.2107 |
| net_avg_win | 59.6847 |
| net_avg_loss | -86.4144 |
| avg_hold_time_bars | 21.1800 |
| exposure | 0.4226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

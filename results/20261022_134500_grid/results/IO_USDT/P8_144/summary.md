# EMA Hourly Continuation — IO/USDT P8_144

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6656 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -3.1289 |
| sortino_ratio | -0.9862 |
| max_drawdown | 0.7014 |
| cagr | -0.3754 |
| net_avg_win | 60.3665 |
| net_avg_loss | -79.5423 |
| avg_hold_time_bars | 32.9387 |
| exposure | 0.7543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

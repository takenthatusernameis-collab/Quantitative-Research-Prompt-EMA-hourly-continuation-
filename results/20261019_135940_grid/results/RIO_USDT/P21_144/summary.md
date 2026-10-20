# EMA Hourly Continuation — RIO/USDT P21_144

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -4.3523 |
| sortino_ratio | -1.5614 |
| max_drawdown | 0.8652 |
| cagr | -0.5278 |
| net_avg_win | 50.6073 |
| net_avg_loss | -62.3618 |
| avg_hold_time_bars | 17.3492 |
| exposure | 0.5177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

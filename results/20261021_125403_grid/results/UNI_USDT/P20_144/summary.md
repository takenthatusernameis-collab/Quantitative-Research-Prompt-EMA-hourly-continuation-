# EMA Hourly Continuation — UNI/USDT P20_144

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.8610 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0321 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -0.8070 |
| sortino_ratio | -0.2127 |
| max_drawdown | 0.2699 |
| cagr | -0.0954 |
| net_avg_win | 79.6631 |
| net_avg_loss | -97.0118 |
| avg_hold_time_bars | 33.8698 |
| exposure | 0.5204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

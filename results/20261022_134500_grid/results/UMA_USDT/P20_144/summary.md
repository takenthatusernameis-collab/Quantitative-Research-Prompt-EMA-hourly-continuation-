# EMA Hourly Continuation — UMA/USDT P20_144

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6307 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9016 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.9541 |
| sortino_ratio | -0.9459 |
| max_drawdown | 0.6860 |
| cagr | -0.3607 |
| net_avg_win | 46.4765 |
| net_avg_loss | -67.9361 |
| avg_hold_time_bars | 22.4255 |
| exposure | 0.5270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

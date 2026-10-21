# EMA Hourly Continuation — APT/USDT P12_26

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.2746 |
| sortino_ratio | -0.6464 |
| max_drawdown | 0.5366 |
| cagr | -0.2560 |
| net_avg_win | 58.0248 |
| net_avg_loss | -81.5055 |
| avg_hold_time_bars | 6.2468 |
| exposure | 0.1116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

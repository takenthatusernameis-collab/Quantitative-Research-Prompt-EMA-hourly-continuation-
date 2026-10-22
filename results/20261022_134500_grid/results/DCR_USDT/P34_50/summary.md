# EMA Hourly Continuation — DCR/USDT P34_50

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.3701 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.8777 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -9.8287 |
| sortino_ratio | -4.2507 |
| max_drawdown | 0.9957 |
| cagr | -0.8830 |
| net_avg_win | 15.6377 |
| net_avg_loss | -28.9448 |
| avg_hold_time_bars | 3.2098 |
| exposure | 0.1336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

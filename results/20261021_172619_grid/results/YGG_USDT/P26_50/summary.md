# EMA Hourly Continuation — YGG/USDT P26_50

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.3747 |
| sortino_ratio | -0.7208 |
| max_drawdown | 0.5683 |
| cagr | -0.2811 |
| net_avg_win | 61.7032 |
| net_avg_loss | -82.2444 |
| avg_hold_time_bars | 6.0730 |
| exposure | 0.1242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DGB/USDT P20_50

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.4291 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -9.4783 |
| sortino_ratio | -4.4456 |
| max_drawdown | 0.9965 |
| cagr | -0.8941 |
| net_avg_win | 16.1043 |
| net_avg_loss | -26.9751 |
| avg_hold_time_bars | 4.2797 |
| exposure | 0.2163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

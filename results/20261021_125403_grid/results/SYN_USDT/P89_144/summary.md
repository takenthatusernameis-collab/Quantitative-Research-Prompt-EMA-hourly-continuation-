# EMA Hourly Continuation — SYN/USDT P89_144

**Symbol:** SYN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7609 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.3770 |
| sortino_ratio | -0.3260 |
| max_drawdown | 0.3253 |
| cagr | -0.1393 |
| net_avg_win | 73.4720 |
| net_avg_loss | -95.8491 |
| avg_hold_time_bars | 8.9341 |
| exposure | 0.1109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — BDX/USDT P26_50

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1427 |
| net_profit_factor | 0.2183 |
| net_win_rate | 0.2390 |
| gross_profit_factor | 0.6569 |
| gross_win_rate | 0.3153 |
| sharpe_ratio | -21.8795 |
| sortino_ratio | -12.9852 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 8.1873 |
| net_avg_loss | -11.7789 |
| avg_hold_time_bars | 2.4639 |
| exposure | 0.1598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

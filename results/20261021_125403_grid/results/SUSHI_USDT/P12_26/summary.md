# EMA Hourly Continuation — SUSHI/USDT P12_26

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8946 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.3585 |
| sortino_ratio | -1.0746 |
| max_drawdown | 0.7177 |
| cagr | -0.3897 |
| net_avg_win | 55.2770 |
| net_avg_loss | -74.2871 |
| avg_hold_time_bars | 5.0575 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

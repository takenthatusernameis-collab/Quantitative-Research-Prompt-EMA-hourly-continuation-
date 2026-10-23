# EMA Hourly Continuation — T/USDT P34_200

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6247 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.8406 |
| sortino_ratio | -0.7737 |
| max_drawdown | 0.6103 |
| cagr | -0.3065 |
| net_avg_win | 57.0108 |
| net_avg_loss | -80.7141 |
| avg_hold_time_bars | 28.6613 |
| exposure | 0.4864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ALEX/USDT P34_89

**Symbol:** ALEX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.4979 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4070 |
| sharpe_ratio | -6.2394 |
| sortino_ratio | -2.0766 |
| max_drawdown | 0.9276 |
| cagr | -0.6420 |
| net_avg_win | 41.0931 |
| net_avg_loss | -53.0419 |
| avg_hold_time_bars | 11.0614 |
| exposure | 0.2866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

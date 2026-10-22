# EMA Hourly Continuation — XLM/USDT P8_34

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1482 |
| net_profit_factor | 0.2701 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.7837 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -10.4211 |
| sortino_ratio | -5.6291 |
| max_drawdown | 0.9993 |
| cagr | -0.9434 |
| net_avg_win | 5.6099 |
| net_avg_loss | -16.6337 |
| avg_hold_time_bars | 4.8401 |
| exposure | 0.3260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

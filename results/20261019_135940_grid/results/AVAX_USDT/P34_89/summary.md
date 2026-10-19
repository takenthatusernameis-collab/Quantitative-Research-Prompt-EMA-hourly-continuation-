# EMA Hourly Continuation — AVAX/USDT P34_89

**Symbol:** AVAX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -5.2283 |
| sortino_ratio | -1.8915 |
| max_drawdown | 0.9108 |
| cagr | -0.6072 |
| net_avg_win | 40.0398 |
| net_avg_loss | -60.2664 |
| avg_hold_time_bars | 7.0790 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

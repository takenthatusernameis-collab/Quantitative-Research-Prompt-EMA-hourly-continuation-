# EMA Hourly Continuation — BICO/USDT P12_89

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.8715 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.0079 |
| sortino_ratio | -0.3342 |
| max_drawdown | 0.4015 |
| cagr | -0.1465 |
| net_avg_win | 81.2500 |
| net_avg_loss | -98.2523 |
| avg_hold_time_bars | 23.0075 |
| exposure | 0.5585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

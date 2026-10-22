# EMA Hourly Continuation — JUP/USDT P12_89

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 792 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.6411 |
| sortino_ratio | -1.8242 |
| max_drawdown | 0.8976 |
| cagr | -0.5867 |
| net_avg_win | 38.9243 |
| net_avg_loss | -53.4954 |
| avg_hold_time_bars | 13.6831 |
| exposure | 0.4926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

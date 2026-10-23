# EMA Hourly Continuation — CSPR/USDT P55_89

**Symbol:** CSPR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.3393 |
| net_win_rate | 0.3914 |
| gross_profit_factor | 0.6922 |
| gross_win_rate | 0.3989 |
| sharpe_ratio | -9.7322 |
| sortino_ratio | -4.1982 |
| max_drawdown | 0.9953 |
| cagr | -0.8806 |
| net_avg_win | 14.1211 |
| net_avg_loss | -26.7561 |
| avg_hold_time_bars | 3.3989 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

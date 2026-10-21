# EMA Hourly Continuation — TNSR/USDT P26_55

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7557 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.9936 |
| sortino_ratio | -0.6337 |
| max_drawdown | 0.5591 |
| cagr | -0.2522 |
| net_avg_win | 64.7916 |
| net_avg_loss | -86.7884 |
| avg_hold_time_bars | 7.1886 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

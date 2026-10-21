# EMA Hourly Continuation — HNT/USDT P89_100

**Symbol:** HNT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 114 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.2844 |
| sortino_ratio | -0.1959 |
| max_drawdown | 0.2211 |
| cagr | -0.0858 |
| net_avg_win | 75.3550 |
| net_avg_loss | -101.4458 |
| avg_hold_time_bars | 10.4211 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

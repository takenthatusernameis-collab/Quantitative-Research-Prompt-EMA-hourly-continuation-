# EMA Hourly Continuation — KAVA/USDT P12_100

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7384 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9994 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.3829 |
| sortino_ratio | -0.7649 |
| max_drawdown | 0.6171 |
| cagr | -0.2987 |
| net_avg_win | 66.5865 |
| net_avg_loss | -88.0634 |
| avg_hold_time_bars | 26.1502 |
| exposure | 0.6015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

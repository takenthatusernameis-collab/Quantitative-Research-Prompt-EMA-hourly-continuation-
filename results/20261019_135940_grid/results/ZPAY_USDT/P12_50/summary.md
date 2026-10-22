# EMA Hourly Continuation — ZPAY/USDT P12_50

**Symbol:** ZPAY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 843 |
| net_profit_factor | 0.4938 |
| net_win_rate | 0.3440 |
| gross_profit_factor | 0.6849 |
| gross_win_rate | 0.3452 |
| sharpe_ratio | -8.1757 |
| sortino_ratio | -3.3036 |
| max_drawdown | 0.9818 |
| cagr | -0.7919 |
| net_avg_win | 32.9946 |
| net_avg_loss | -35.0410 |
| avg_hold_time_bars | 10.0142 |
| exposure | 0.3820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

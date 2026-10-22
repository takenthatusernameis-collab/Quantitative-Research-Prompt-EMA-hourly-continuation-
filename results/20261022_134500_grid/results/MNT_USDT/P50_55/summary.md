# EMA Hourly Continuation — MNT/USDT P50_55

**Symbol:** MNT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.0943 |
| net_win_rate | 0.2671 |
| gross_profit_factor | 0.4918 |
| gross_win_rate | 0.3519 |
| sharpe_ratio | -15.2685 |
| sortino_ratio | -6.6970 |
| max_drawdown | 0.9999 |
| cagr | -0.9774 |
| net_avg_win | 4.9314 |
| net_avg_loss | -19.0670 |
| avg_hold_time_bars | 2.0759 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

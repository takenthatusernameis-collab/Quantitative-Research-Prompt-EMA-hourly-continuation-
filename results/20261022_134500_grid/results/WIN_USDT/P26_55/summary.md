# EMA Hourly Continuation — WIN/USDT P26_55

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.3051 |
| net_win_rate | 0.3922 |
| gross_profit_factor | 0.7860 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -10.0892 |
| sortino_ratio | -4.1992 |
| max_drawdown | 0.9959 |
| cagr | -0.8870 |
| net_avg_win | 13.1279 |
| net_avg_loss | -27.7708 |
| avg_hold_time_bars | 4.3757 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

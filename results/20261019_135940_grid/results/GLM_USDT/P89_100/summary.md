# EMA Hourly Continuation — GLM/USDT P89_100

**Symbol:** GLM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.2470 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.7522 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -9.0844 |
| sortino_ratio | -3.2713 |
| max_drawdown | 0.9849 |
| cagr | -0.8110 |
| net_avg_win | 13.5710 |
| net_avg_loss | -34.7808 |
| avg_hold_time_bars | 3.1010 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

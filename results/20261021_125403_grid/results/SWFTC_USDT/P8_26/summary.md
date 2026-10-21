# EMA Hourly Continuation — SWFTC/USDT P8_26

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7710 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -2.1096 |
| sortino_ratio | -0.7237 |
| max_drawdown | 0.5849 |
| cagr | -0.2829 |
| net_avg_win | 66.2011 |
| net_avg_loss | -87.3758 |
| avg_hold_time_bars | 7.3520 |
| exposure | 0.1908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

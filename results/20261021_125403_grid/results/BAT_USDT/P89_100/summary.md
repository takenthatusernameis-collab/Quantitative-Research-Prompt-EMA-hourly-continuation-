# EMA Hourly Continuation — BAT/USDT P89_100

**Symbol:** BAT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.8218 |
| sortino_ratio | -0.3338 |
| max_drawdown | 0.3280 |
| cagr | -0.1403 |
| net_avg_win | 64.1787 |
| net_avg_loss | -104.4706 |
| avg_hold_time_bars | 4.5528 |
| exposure | 0.0333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — GLM/USDT P8_55

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.7418 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -2.5985 |
| sortino_ratio | -1.0021 |
| max_drawdown | 0.7083 |
| cagr | -0.3684 |
| net_avg_win | 54.4855 |
| net_avg_loss | -72.8459 |
| avg_hold_time_bars | 15.0414 |
| exposure | 0.4957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

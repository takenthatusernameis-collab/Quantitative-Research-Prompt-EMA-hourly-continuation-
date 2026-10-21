# EMA Hourly Continuation — APE/USDT P20_100

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9501 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.7655 |
| sortino_ratio | -0.5485 |
| max_drawdown | 0.5076 |
| cagr | -0.2235 |
| net_avg_win | 68.2219 |
| net_avg_loss | -84.5482 |
| avg_hold_time_bars | 17.5159 |
| exposure | 0.3766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

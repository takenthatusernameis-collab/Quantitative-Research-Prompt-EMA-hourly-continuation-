# EMA Hourly Continuation — GMT/USDT P21_34

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6183 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -2.4958 |
| sortino_ratio | -0.6222 |
| max_drawdown | 0.5176 |
| cagr | -0.2475 |
| net_avg_win | 57.8098 |
| net_avg_loss | -83.5697 |
| avg_hold_time_bars | 4.9043 |
| exposure | 0.0675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

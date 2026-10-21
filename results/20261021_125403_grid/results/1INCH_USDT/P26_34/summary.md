# EMA Hourly Continuation — 1INCH/USDT P26_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.4919 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.7735 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -3.3361 |
| sortino_ratio | -0.7304 |
| max_drawdown | 0.5719 |
| cagr | -0.2867 |
| net_avg_win | 54.2694 |
| net_avg_loss | -85.9115 |
| avg_hold_time_bars | 4.4421 |
| exposure | 0.0470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

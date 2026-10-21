# EMA Hourly Continuation — CAKE/USDT P34_89

**Symbol:** CAKE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8015 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1117 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -1.3434 |
| sortino_ratio | -0.3835 |
| max_drawdown | 0.4246 |
| cagr | -0.1624 |
| net_avg_win | 70.0607 |
| net_avg_loss | -97.2801 |
| avg_hold_time_bars | 14.2697 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

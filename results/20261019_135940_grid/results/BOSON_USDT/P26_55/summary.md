# EMA Hourly Continuation — BOSON/USDT P26_55

**Symbol:** BOSON/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -5.6795 |
| sortino_ratio | -2.3177 |
| max_drawdown | 0.9411 |
| cagr | -0.6750 |
| net_avg_win | 29.4730 |
| net_avg_loss | -44.7250 |
| avg_hold_time_bars | 5.3274 |
| exposure | 0.2056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

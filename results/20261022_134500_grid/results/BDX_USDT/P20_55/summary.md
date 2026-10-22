# EMA Hourly Continuation — BDX/USDT P20_55

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1358 |
| net_profit_factor | 0.2678 |
| net_win_rate | 0.2651 |
| gross_profit_factor | 0.6677 |
| gross_win_rate | 0.3284 |
| sharpe_ratio | -19.7790 |
| sortino_ratio | -11.0868 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 10.1616 |
| net_avg_loss | -13.6855 |
| avg_hold_time_bars | 3.9359 |
| exposure | 0.2430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

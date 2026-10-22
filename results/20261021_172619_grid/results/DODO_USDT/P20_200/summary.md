# EMA Hourly Continuation — DODO/USDT P20_200

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6575 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.7923 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -2.7089 |
| sortino_ratio | -0.7285 |
| max_drawdown | 0.5920 |
| cagr | -0.2851 |
| net_avg_win | 69.3694 |
| net_avg_loss | -80.9273 |
| avg_hold_time_bars | 35.8901 |
| exposure | 0.5912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CARV/USDT P12_100

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7181 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.3627 |
| sortino_ratio | -0.7351 |
| max_drawdown | 0.5343 |
| cagr | -0.2880 |
| net_avg_win | 70.0841 |
| net_avg_loss | -85.7527 |
| avg_hold_time_bars | 24.7881 |
| exposure | 0.5398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

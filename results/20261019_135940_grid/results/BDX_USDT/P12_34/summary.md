# EMA Hourly Continuation — BDX/USDT P12_34

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1693 |
| net_profit_factor | 0.2343 |
| net_win_rate | 0.2357 |
| gross_profit_factor | 0.6691 |
| gross_win_rate | 0.3083 |
| sharpe_ratio | -23.7409 |
| sortino_ratio | -15.1273 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 7.6701 |
| net_avg_loss | -10.0930 |
| avg_hold_time_bars | 2.5836 |
| exposure | 0.1988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

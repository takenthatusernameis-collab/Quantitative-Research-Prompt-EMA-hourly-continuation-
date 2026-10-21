# EMA Hourly Continuation — 1INCH/USDT P12_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7280 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.2031 |
| sortino_ratio | -0.6504 |
| max_drawdown | 0.5473 |
| cagr | -0.2592 |
| net_avg_win | 69.0954 |
| net_avg_loss | -86.8627 |
| avg_hold_time_bars | 32.5291 |
| exposure | 0.6343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

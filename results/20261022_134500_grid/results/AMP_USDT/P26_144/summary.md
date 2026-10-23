# EMA Hourly Continuation — AMP/USDT P26_144

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.3858 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.6482 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -7.4241 |
| sortino_ratio | -2.8958 |
| max_drawdown | 0.9742 |
| cagr | -0.7610 |
| net_avg_win | 19.7688 |
| net_avg_loss | -34.1982 |
| avg_hold_time_bars | 13.5855 |
| exposure | 0.4767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

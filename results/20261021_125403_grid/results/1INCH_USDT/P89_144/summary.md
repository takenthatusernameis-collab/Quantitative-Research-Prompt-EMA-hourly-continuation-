# EMA Hourly Continuation — 1INCH/USDT P89_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6183 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -2.4437 |
| sortino_ratio | -0.5725 |
| max_drawdown | 0.4959 |
| cagr | -0.2311 |
| net_avg_win | 62.0961 |
| net_avg_loss | -89.1174 |
| avg_hold_time_bars | 8.7351 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — WOO/USDT P34_144

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7108 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9986 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -2.5529 |
| sortino_ratio | -0.7486 |
| max_drawdown | 0.6111 |
| cagr | -0.2999 |
| net_avg_win | 69.2299 |
| net_avg_loss | -90.5007 |
| avg_hold_time_bars | 21.6009 |
| exposure | 0.4281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TRADE/USDT P89_144

**Symbol:** TRADE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.3980 |
| net_win_rate | 0.3778 |
| gross_profit_factor | 0.6149 |
| gross_win_rate | 0.3829 |
| sharpe_ratio | -5.5468 |
| sortino_ratio | -1.5607 |
| max_drawdown | 0.8539 |
| cagr | -0.5319 |
| net_avg_win | 37.5207 |
| net_avg_loss | -57.2551 |
| avg_hold_time_bars | 5.9698 |
| exposure | 0.1077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

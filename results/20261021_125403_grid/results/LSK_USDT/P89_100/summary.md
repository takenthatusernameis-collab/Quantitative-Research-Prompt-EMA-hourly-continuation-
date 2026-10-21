# EMA Hourly Continuation — LSK/USDT P89_100

**Symbol:** LSK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5788 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9889 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -2.7054 |
| sortino_ratio | -0.5819 |
| max_drawdown | 0.5193 |
| cagr | -0.2383 |
| net_avg_win | 62.4234 |
| net_avg_loss | -99.6313 |
| avg_hold_time_bars | 5.5595 |
| exposure | 0.0574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

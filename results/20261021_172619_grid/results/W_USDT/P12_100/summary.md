# EMA Hourly Continuation — W/USDT P12_100

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.9416 |
| net_win_rate | 0.5295 |
| gross_profit_factor | 1.1080 |
| gross_win_rate | 0.5295 |
| sharpe_ratio | -0.3197 |
| sortino_ratio | -0.0985 |
| max_drawdown | 0.2267 |
| cagr | -0.0508 |
| net_avg_win | 81.8169 |
| net_avg_loss | -97.8004 |
| avg_hold_time_bars | 28.1313 |
| exposure | 0.5844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

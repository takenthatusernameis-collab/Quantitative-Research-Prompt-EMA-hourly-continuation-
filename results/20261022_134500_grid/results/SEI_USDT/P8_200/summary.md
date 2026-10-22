# EMA Hourly Continuation — SEI/USDT P8_200

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.1013 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -1.1934 |
| sortino_ratio | -0.2848 |
| max_drawdown | 0.3595 |
| cagr | -0.1302 |
| net_avg_win | 82.1759 |
| net_avg_loss | -111.9280 |
| avg_hold_time_bars | 63.7310 |
| exposure | 0.8401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

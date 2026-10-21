# EMA Hourly Continuation — XDC/USDT P21_200

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8155 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0500 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.2096 |
| sortino_ratio | -0.3240 |
| max_drawdown | 0.3313 |
| cagr | -0.1391 |
| net_avg_win | 77.8348 |
| net_avg_loss | -99.3521 |
| avg_hold_time_bars | 34.5788 |
| exposure | 0.5485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — REQ/USDT P55_144

**Symbol:** REQ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5596 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8162 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -3.9790 |
| sortino_ratio | -1.1049 |
| max_drawdown | 0.7395 |
| cagr | -0.4020 |
| net_avg_win | 56.1782 |
| net_avg_loss | -76.5744 |
| avg_hold_time_bars | 13.1794 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

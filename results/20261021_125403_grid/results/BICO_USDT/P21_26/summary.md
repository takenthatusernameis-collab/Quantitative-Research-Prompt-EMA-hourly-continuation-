# EMA Hourly Continuation — BICO/USDT P21_26

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -3.1299 |
| sortino_ratio | -0.8299 |
| max_drawdown | 0.6174 |
| cagr | -0.3169 |
| net_avg_win | 53.2057 |
| net_avg_loss | -79.0281 |
| avg_hold_time_bars | 4.7616 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

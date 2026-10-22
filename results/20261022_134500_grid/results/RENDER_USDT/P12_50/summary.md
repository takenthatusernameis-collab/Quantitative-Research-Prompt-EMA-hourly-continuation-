# EMA Hourly Continuation — RENDER/USDT P12_50

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.5595 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8652 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -6.6863 |
| sortino_ratio | -3.2230 |
| max_drawdown | 0.9696 |
| cagr | -0.7926 |
| net_avg_win | 25.9600 |
| net_avg_loss | -40.1941 |
| avg_hold_time_bars | 5.8184 |
| exposure | 0.3129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

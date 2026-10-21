# EMA Hourly Continuation — LQTY/USDT P12_100

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8288 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0211 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -1.2066 |
| sortino_ratio | -0.3702 |
| max_drawdown | 0.3834 |
| cagr | -0.1586 |
| net_avg_win | 73.0335 |
| net_avg_loss | -91.2429 |
| avg_hold_time_bars | 28.9717 |
| exposure | 0.6031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

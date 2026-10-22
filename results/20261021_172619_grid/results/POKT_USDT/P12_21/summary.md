# EMA Hourly Continuation — POKT/USDT P12_21

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5179 |
| net_win_rate | 0.3805 |
| gross_profit_factor | 0.7264 |
| gross_win_rate | 0.3805 |
| sharpe_ratio | -5.5258 |
| sortino_ratio | -1.6996 |
| max_drawdown | 0.8724 |
| cagr | -0.5458 |
| net_avg_win | 51.5301 |
| net_avg_loss | -61.1242 |
| avg_hold_time_bars | 5.2727 |
| exposure | 0.1129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MERL/USDT P12_89

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.9105 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0559 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -0.6865 |
| sortino_ratio | -0.2190 |
| max_drawdown | 0.3762 |
| cagr | -0.1007 |
| net_avg_win | 94.2249 |
| net_avg_loss | -108.6630 |
| avg_hold_time_bars | 25.8394 |
| exposure | 0.5795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

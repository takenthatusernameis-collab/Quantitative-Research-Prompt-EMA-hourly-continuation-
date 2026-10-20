# EMA Hourly Continuation — POPCAT/USDT P89_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7801 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0402 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.5236 |
| sortino_ratio | -0.4363 |
| max_drawdown | 0.3802 |
| cagr | -0.1843 |
| net_avg_win | 71.7794 |
| net_avg_loss | -95.2557 |
| avg_hold_time_bars | 11.9769 |
| exposure | 0.2189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

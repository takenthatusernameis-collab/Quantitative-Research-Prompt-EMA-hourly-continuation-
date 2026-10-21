# EMA Hourly Continuation — FLOKI/USDT P8_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.9134 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -0.4494 |
| sortino_ratio | -0.1137 |
| max_drawdown | 0.2438 |
| cagr | -0.0546 |
| net_avg_win | 86.6401 |
| net_avg_loss | -101.1763 |
| avg_hold_time_bars | 55.0935 |
| exposure | 0.7763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

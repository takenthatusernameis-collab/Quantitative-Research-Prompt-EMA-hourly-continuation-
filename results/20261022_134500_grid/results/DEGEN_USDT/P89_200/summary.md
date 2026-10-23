# EMA Hourly Continuation — DEGEN/USDT P89_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7738 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.1060 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -1.7439 |
| sortino_ratio | -0.4687 |
| max_drawdown | 0.4723 |
| cagr | -0.2049 |
| net_avg_win | 79.1302 |
| net_avg_loss | -108.5828 |
| avg_hold_time_bars | 13.2589 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

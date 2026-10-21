# EMA Hourly Continuation — CATI/USDT P12_200

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7510 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -2.2811 |
| sortino_ratio | -0.5080 |
| max_drawdown | 0.4508 |
| cagr | -0.2103 |
| net_avg_win | 72.3047 |
| net_avg_loss | -88.8189 |
| avg_hold_time_bars | 67.1401 |
| exposure | 0.7618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

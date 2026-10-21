# EMA Hourly Continuation — ARKM/USDT P8_200

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.8263 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -0.9621 |
| sortino_ratio | -0.2252 |
| max_drawdown | 0.3038 |
| cagr | -0.1001 |
| net_avg_win | 84.5052 |
| net_avg_loss | -95.6975 |
| avg_hold_time_bars | 66.0111 |
| exposure | 0.8131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

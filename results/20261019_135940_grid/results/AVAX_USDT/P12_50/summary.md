# EMA Hourly Continuation — AVAX/USDT P12_50

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.6125 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 1.0153 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -7.1158 |
| sortino_ratio | -3.2461 |
| max_drawdown | 0.9824 |
| cagr | -0.7943 |
| net_avg_win | 32.7160 |
| net_avg_loss | -44.0327 |
| avg_hold_time_bars | 7.1544 |
| exposure | 0.3411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

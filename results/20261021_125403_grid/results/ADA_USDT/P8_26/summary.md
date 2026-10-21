# EMA Hourly Continuation — ADA/USDT P8_26

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7672 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -1.9503 |
| sortino_ratio | -0.7007 |
| max_drawdown | 0.5938 |
| cagr | -0.2749 |
| net_avg_win | 56.5158 |
| net_avg_loss | -79.8461 |
| avg_hold_time_bars | 5.9565 |
| exposure | 0.1681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

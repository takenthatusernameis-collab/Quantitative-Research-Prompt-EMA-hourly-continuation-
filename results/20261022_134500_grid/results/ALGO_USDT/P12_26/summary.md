# EMA Hourly Continuation — ALGO/USDT P12_26

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1399 |
| net_profit_factor | 0.3886 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -10.3567 |
| sortino_ratio | -5.4353 |
| max_drawdown | 0.9991 |
| cagr | -0.9387 |
| net_avg_win | 10.0806 |
| net_avg_loss | -21.2507 |
| avg_hold_time_bars | 2.8499 |
| exposure | 0.1812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

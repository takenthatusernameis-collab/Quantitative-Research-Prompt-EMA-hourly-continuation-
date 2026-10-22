# EMA Hourly Continuation — OSMO/USDT P8_50

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.7204 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9442 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -3.4757 |
| sortino_ratio | -1.3455 |
| max_drawdown | 0.8016 |
| cagr | -0.4613 |
| net_avg_win | 58.8920 |
| net_avg_loss | -71.5802 |
| avg_hold_time_bars | 13.1786 |
| exposure | 0.4427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

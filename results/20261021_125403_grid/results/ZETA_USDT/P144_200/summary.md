# EMA Hourly Continuation — ZETA/USDT P144_200

**Symbol:** ZETA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6506 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -2.1147 |
| sortino_ratio | -0.4569 |
| max_drawdown | 0.4591 |
| cagr | -0.1892 |
| net_avg_win | 71.5057 |
| net_avg_loss | -95.6066 |
| avg_hold_time_bars | 7.5609 |
| exposure | 0.0787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DODO/USDT P8_26

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1576 |
| net_profit_factor | 0.4574 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -9.7816 |
| sortino_ratio | -5.4476 |
| max_drawdown | 0.9988 |
| cagr | -0.9306 |
| net_avg_win | 12.3443 |
| net_avg_loss | -20.5893 |
| avg_hold_time_bars | 4.2113 |
| exposure | 0.3003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

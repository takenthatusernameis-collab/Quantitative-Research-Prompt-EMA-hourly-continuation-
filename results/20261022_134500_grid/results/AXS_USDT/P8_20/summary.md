# EMA Hourly Continuation — AXS/USDT P8_20

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1616 |
| net_profit_factor | 0.2538 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.6597 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -12.6053 |
| sortino_ratio | -7.1499 |
| max_drawdown | 0.9999 |
| cagr | -0.9741 |
| net_avg_win | 4.9806 |
| net_avg_loss | -14.3631 |
| avg_hold_time_bars | 2.9604 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

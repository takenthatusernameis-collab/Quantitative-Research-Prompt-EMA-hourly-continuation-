# EMA Hourly Continuation — XNO/USDT P50_144

**Symbol:** XNO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.5259 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.8592 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -6.1901 |
| sortino_ratio | -2.2441 |
| max_drawdown | 0.9333 |
| cagr | -0.6598 |
| net_avg_win | 37.9212 |
| net_avg_loss | -51.1311 |
| avg_hold_time_bars | 9.4088 |
| exposure | 0.2814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

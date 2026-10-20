# EMA Hourly Continuation — WOO/USDT P8_12

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1832 |
| net_profit_factor | 0.2163 |
| net_win_rate | 0.3646 |
| gross_profit_factor | 0.6589 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -17.0714 |
| sortino_ratio | -10.4896 |
| max_drawdown | 1.0000 |
| cagr | -0.9962 |
| net_avg_win | 4.1324 |
| net_avg_loss | -10.9626 |
| avg_hold_time_bars | 2.0857 |
| exposure | 0.1737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

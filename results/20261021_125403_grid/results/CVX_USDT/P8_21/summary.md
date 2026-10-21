# EMA Hourly Continuation — CVX/USDT P8_21

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7433 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0221 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -2.3714 |
| sortino_ratio | -0.8849 |
| max_drawdown | 0.6455 |
| cagr | -0.3328 |
| net_avg_win | 54.0342 |
| net_avg_loss | -74.8811 |
| avg_hold_time_bars | 5.7166 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

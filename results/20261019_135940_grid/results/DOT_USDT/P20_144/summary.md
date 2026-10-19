# EMA Hourly Continuation — DOT/USDT P20_144

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.6425 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -3.0246 |
| sortino_ratio | -0.8899 |
| max_drawdown | 0.6895 |
| cagr | -0.3519 |
| net_avg_win | 56.2412 |
| net_avg_loss | -81.0399 |
| avg_hold_time_bars | 28.3492 |
| exposure | 0.5683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

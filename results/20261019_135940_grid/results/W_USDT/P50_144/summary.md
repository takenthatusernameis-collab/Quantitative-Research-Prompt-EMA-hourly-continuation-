# EMA Hourly Continuation — W/USDT P50_144

**Symbol:** W/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6759 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5566 |
| sortino_ratio | -0.7821 |
| max_drawdown | 0.6308 |
| cagr | -0.3095 |
| net_avg_win | 54.6438 |
| net_avg_loss | -78.8045 |
| avg_hold_time_bars | 13.0577 |
| exposure | 0.2778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

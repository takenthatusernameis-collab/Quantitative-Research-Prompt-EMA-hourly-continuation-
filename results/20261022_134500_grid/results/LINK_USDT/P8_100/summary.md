# EMA Hourly Continuation — LINK/USDT P8_100

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0475 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -3.3885 |
| sortino_ratio | -1.1759 |
| max_drawdown | 0.7693 |
| cagr | -0.4335 |
| net_avg_win | 56.2439 |
| net_avg_loss | -79.5653 |
| avg_hold_time_bars | 23.9869 |
| exposure | 0.6662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

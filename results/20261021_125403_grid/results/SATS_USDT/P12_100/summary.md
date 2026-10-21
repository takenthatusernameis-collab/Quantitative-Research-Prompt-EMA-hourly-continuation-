# EMA Hourly Continuation — SATS/USDT P12_100

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8044 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9759 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.5818 |
| sortino_ratio | -0.4935 |
| max_drawdown | 0.5284 |
| cagr | -0.2047 |
| net_avg_win | 76.4804 |
| net_avg_loss | -91.9596 |
| avg_hold_time_bars | 25.4000 |
| exposure | 0.5517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

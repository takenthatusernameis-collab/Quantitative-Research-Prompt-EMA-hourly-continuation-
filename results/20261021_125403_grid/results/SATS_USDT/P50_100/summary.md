# EMA Hourly Continuation — SATS/USDT P50_100

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6599 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.6826 |
| sortino_ratio | -0.7450 |
| max_drawdown | 0.6055 |
| cagr | -0.2888 |
| net_avg_win | 64.3174 |
| net_avg_loss | -81.1417 |
| avg_hold_time_bars | 9.1697 |
| exposure | 0.1589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

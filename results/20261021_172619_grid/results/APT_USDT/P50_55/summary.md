# EMA Hourly Continuation — APT/USDT P50_55

**Symbol:** APT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.7621 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0589 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.7745 |
| sortino_ratio | -0.1065 |
| max_drawdown | 0.1352 |
| cagr | -0.0474 |
| net_avg_win | 78.2407 |
| net_avg_loss | -109.6698 |
| avg_hold_time_bars | 5.0330 |
| exposure | 0.0208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

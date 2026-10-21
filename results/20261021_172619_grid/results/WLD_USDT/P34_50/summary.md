# EMA Hourly Continuation — WLD/USDT P34_50

**Symbol:** WLD/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.8195 |
| net_win_rate | 0.5213 |
| gross_profit_factor | 1.0703 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -0.8325 |
| sortino_ratio | -0.1743 |
| max_drawdown | 0.2538 |
| cagr | -0.0775 |
| net_avg_win | 75.6303 |
| net_avg_loss | -100.5172 |
| avg_hold_time_bars | 5.6256 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

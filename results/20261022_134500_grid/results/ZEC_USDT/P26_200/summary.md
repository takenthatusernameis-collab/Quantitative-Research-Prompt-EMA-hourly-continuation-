# EMA Hourly Continuation — ZEC/USDT P26_200

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8919 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1254 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.6146 |
| sortino_ratio | -0.1630 |
| max_drawdown | 0.3018 |
| cagr | -0.0753 |
| net_avg_win | 81.8678 |
| net_avg_loss | -103.2627 |
| avg_hold_time_bars | 36.8265 |
| exposure | 0.5691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

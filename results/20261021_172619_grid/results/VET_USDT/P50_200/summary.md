# EMA Hourly Continuation — VET/USDT P50_200

**Symbol:** VET/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8305 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0435 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -1.0155 |
| sortino_ratio | -0.2530 |
| max_drawdown | 0.2996 |
| cagr | -0.1113 |
| net_avg_win | 81.1147 |
| net_avg_loss | -102.9802 |
| avg_hold_time_bars | 27.5828 |
| exposure | 0.3786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

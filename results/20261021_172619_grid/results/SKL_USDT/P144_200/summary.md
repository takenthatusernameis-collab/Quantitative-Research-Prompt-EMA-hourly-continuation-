# EMA Hourly Continuation — SKL/USDT P144_200

**Symbol:** SKL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.8492 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1371 |
| gross_win_rate | 0.5373 |
| sharpe_ratio | -0.6359 |
| sortino_ratio | -0.1305 |
| max_drawdown | 0.1996 |
| cagr | -0.0593 |
| net_avg_win | 74.2025 |
| net_avg_loss | -101.4740 |
| avg_hold_time_bars | 8.0547 |
| exposure | 0.0736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

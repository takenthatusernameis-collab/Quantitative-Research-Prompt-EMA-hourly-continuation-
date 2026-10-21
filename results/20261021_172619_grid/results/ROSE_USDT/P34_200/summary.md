# EMA Hourly Continuation — ROSE/USDT P34_200

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 1.0394 |
| net_win_rate | 0.5515 |
| gross_profit_factor | 1.2144 |
| gross_win_rate | 0.5515 |
| sharpe_ratio | 0.2427 |
| sortino_ratio | 0.0581 |
| max_drawdown | 0.1040 |
| cagr | 0.0200 |
| net_avg_win | 89.6765 |
| net_avg_loss | -106.0779 |
| avg_hold_time_bars | 44.5404 |
| exposure | 0.5507 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

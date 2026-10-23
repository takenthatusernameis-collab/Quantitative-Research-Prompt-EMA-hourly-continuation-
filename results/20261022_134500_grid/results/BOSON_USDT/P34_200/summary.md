# EMA Hourly Continuation — BOSON/USDT P34_200

**Symbol:** BOSON/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7458 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.0587 |
| sortino_ratio | -0.6324 |
| max_drawdown | 0.5215 |
| cagr | -0.2544 |
| net_avg_win | 68.3025 |
| net_avg_loss | -83.7333 |
| avg_hold_time_bars | 21.1876 |
| exposure | 0.4517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

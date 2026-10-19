# EMA Hourly Continuation — AVAX/USDT P50_89

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.5239 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -6.2501 |
| sortino_ratio | -2.2150 |
| max_drawdown | 0.9434 |
| cagr | -0.6761 |
| net_avg_win | 35.7067 |
| net_avg_loss | -55.9921 |
| avg_hold_time_bars | 4.3888 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

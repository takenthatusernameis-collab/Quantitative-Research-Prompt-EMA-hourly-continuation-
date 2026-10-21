# EMA Hourly Continuation — KAVA/USDT P144_200

**Symbol:** KAVA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5142 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -3.2810 |
| sortino_ratio | -0.6990 |
| max_drawdown | 0.5743 |
| cagr | -0.2861 |
| net_avg_win | 60.4394 |
| net_avg_loss | -92.5544 |
| avg_hold_time_bars | 7.8150 |
| exposure | 0.0806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AVAX/USDT P12_21

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8614 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -2.8732 |
| sortino_ratio | -0.6772 |
| max_drawdown | 0.5620 |
| cagr | -0.2673 |
| net_avg_win | 68.7749 |
| net_avg_loss | -92.0727 |
| avg_hold_time_bars | 4.6765 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

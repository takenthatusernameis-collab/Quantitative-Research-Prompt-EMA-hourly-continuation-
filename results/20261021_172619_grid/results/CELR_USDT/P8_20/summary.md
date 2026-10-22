# EMA Hourly Continuation — CELR/USDT P8_20

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -4.6640 |
| sortino_ratio | -1.8165 |
| max_drawdown | 0.8796 |
| cagr | -0.5653 |
| net_avg_win | 38.1757 |
| net_avg_loss | -53.2326 |
| avg_hold_time_bars | 5.1566 |
| exposure | 0.1743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

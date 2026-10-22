# EMA Hourly Continuation — WOO/USDT P8_21

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.7566 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0346 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.8298 |
| sortino_ratio | -1.1061 |
| max_drawdown | 0.7285 |
| cagr | -0.3977 |
| net_avg_win | 60.4889 |
| net_avg_loss | -79.5206 |
| avg_hold_time_bars | 5.4528 |
| exposure | 0.1839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

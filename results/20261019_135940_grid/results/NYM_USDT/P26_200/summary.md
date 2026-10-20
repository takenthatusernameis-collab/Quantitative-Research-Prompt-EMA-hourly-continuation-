# EMA Hourly Continuation — NYM/USDT P26_200

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.3645 |
| net_win_rate | 0.3676 |
| gross_profit_factor | 0.6608 |
| gross_win_rate | 0.3830 |
| sharpe_ratio | -6.2148 |
| sortino_ratio | -1.7216 |
| max_drawdown | 0.8901 |
| cagr | -0.5850 |
| net_avg_win | 35.7060 |
| net_avg_loss | -56.9404 |
| avg_hold_time_bars | 30.8663 |
| exposure | 0.5458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

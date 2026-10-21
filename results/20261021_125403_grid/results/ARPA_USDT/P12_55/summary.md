# EMA Hourly Continuation — ARPA/USDT P12_55

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.7422 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -3.1660 |
| sortino_ratio | -1.2504 |
| max_drawdown | 0.7850 |
| cagr | -0.4354 |
| net_avg_win | 58.7857 |
| net_avg_loss | -75.7587 |
| avg_hold_time_bars | 10.3686 |
| exposure | 0.3589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

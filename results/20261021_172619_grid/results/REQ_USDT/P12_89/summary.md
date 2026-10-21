# EMA Hourly Continuation — REQ/USDT P12_89

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6504 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -3.9851 |
| sortino_ratio | -1.3708 |
| max_drawdown | 0.8045 |
| cagr | -0.4704 |
| net_avg_win | 55.5676 |
| net_avg_loss | -71.7301 |
| avg_hold_time_bars | 18.0103 |
| exposure | 0.4789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

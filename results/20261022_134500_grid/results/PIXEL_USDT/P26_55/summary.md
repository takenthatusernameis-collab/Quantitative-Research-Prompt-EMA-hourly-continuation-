# EMA Hourly Continuation — PIXEL/USDT P26_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 904 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -5.4319 |
| sortino_ratio | -2.3019 |
| max_drawdown | 0.9422 |
| cagr | -0.6699 |
| net_avg_win | 31.3843 |
| net_avg_loss | -47.6129 |
| avg_hold_time_bars | 4.9646 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

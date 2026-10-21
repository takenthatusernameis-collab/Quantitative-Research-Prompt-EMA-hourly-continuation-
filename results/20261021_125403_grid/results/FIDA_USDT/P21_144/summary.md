# EMA Hourly Continuation — FIDA/USDT P21_144

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.0200 |
| sortino_ratio | -0.5857 |
| max_drawdown | 0.5168 |
| cagr | -0.2373 |
| net_avg_win | 64.0687 |
| net_avg_loss | -81.1924 |
| avg_hold_time_bars | 28.1103 |
| exposure | 0.5304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

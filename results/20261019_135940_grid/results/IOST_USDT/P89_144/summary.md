# EMA Hourly Continuation — IOST/USDT P89_144

**Symbol:** IOST/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5159 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0253 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -4.3342 |
| sortino_ratio | -1.3535 |
| max_drawdown | 0.8172 |
| cagr | -0.4850 |
| net_avg_win | 36.0208 |
| net_avg_loss | -67.5633 |
| avg_hold_time_bars | 5.3115 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

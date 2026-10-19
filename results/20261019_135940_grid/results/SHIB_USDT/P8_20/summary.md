# EMA Hourly Continuation — SHIB/USDT P8_20

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1696 |
| net_profit_factor | 0.3161 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7774 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -13.7511 |
| sortino_ratio | -8.0394 |
| max_drawdown | 1.0000 |
| cagr | -0.9847 |
| net_avg_win | 6.4284 |
| net_avg_loss | -14.9660 |
| avg_hold_time_bars | 2.6185 |
| exposure | 0.2019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

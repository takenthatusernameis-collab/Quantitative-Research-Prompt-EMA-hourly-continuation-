# EMA Hourly Continuation — XDC/USDT P50_144

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7014 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.9848 |
| sortino_ratio | -0.5307 |
| max_drawdown | 0.4808 |
| cagr | -0.2151 |
| net_avg_win | 61.1670 |
| net_avg_loss | -88.2131 |
| avg_hold_time_bars | 14.1351 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

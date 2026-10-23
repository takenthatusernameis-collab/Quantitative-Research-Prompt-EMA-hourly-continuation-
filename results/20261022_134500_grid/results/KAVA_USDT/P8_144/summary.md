# EMA Hourly Continuation — KAVA/USDT P8_144

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6273 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -4.2075 |
| sortino_ratio | -1.3856 |
| max_drawdown | 0.8338 |
| cagr | -0.4929 |
| net_avg_win | 53.7909 |
| net_avg_loss | -73.4228 |
| avg_hold_time_bars | 29.8090 |
| exposure | 0.7520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

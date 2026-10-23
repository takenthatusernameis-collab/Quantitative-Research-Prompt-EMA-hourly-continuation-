# EMA Hourly Continuation — PUFFER/USDT P12_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0401 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.5258 |
| sortino_ratio | -0.4807 |
| max_drawdown | 0.4336 |
| cagr | -0.2069 |
| net_avg_win | 68.5751 |
| net_avg_loss | -90.4279 |
| avg_hold_time_bars | 28.9250 |
| exposure | 0.6547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

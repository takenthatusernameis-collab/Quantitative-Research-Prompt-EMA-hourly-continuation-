# EMA Hourly Continuation — SUN/USDT P12_144

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4510 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -5.1196 |
| sortino_ratio | -1.4633 |
| max_drawdown | 0.8435 |
| cagr | -0.5205 |
| net_avg_win | 38.7036 |
| net_avg_loss | -64.5473 |
| avg_hold_time_bars | 36.3357 |
| exposure | 0.6857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — BAT/USDT P20_144

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9556 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.9765 |
| sortino_ratio | -0.9526 |
| max_drawdown | 0.7006 |
| cagr | -0.3619 |
| net_avg_win | 48.4580 |
| net_avg_loss | -71.3239 |
| avg_hold_time_bars | 23.2281 |
| exposure | 0.5416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

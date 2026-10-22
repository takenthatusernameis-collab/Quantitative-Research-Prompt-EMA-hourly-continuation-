# EMA Hourly Continuation — MLK/USDT P8_144

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5980 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7548 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -3.7511 |
| sortino_ratio | -1.1771 |
| max_drawdown | 0.7490 |
| cagr | -0.4198 |
| net_avg_win | 52.8952 |
| net_avg_loss | -64.9478 |
| avg_hold_time_bars | 26.2258 |
| exposure | 0.5887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

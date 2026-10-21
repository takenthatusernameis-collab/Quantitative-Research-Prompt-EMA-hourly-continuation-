# EMA Hourly Continuation — UNI/USDT P12_144

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8364 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0512 |
| sortino_ratio | -0.2850 |
| max_drawdown | 0.3413 |
| cagr | -0.1246 |
| net_avg_win | 80.6544 |
| net_avg_loss | -96.4349 |
| avg_hold_time_bars | 38.5250 |
| exposure | 0.6304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

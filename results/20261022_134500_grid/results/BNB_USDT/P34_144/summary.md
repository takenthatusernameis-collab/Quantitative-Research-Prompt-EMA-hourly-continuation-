# EMA Hourly Continuation — BNB/USDT P34_144

**Symbol:** BNB/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.3892 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9220 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -6.3156 |
| sortino_ratio | -2.1207 |
| max_drawdown | 0.9392 |
| cagr | -0.6678 |
| net_avg_win | 22.2810 |
| net_avg_loss | -49.3347 |
| avg_hold_time_bars | 13.5285 |
| exposure | 0.3560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

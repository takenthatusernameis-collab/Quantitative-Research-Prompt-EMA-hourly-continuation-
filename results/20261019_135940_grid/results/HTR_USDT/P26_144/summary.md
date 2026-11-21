# EMA Hourly Continuation — HTR/USDT P26_144

**Symbol:** HTR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7638 |
| gross_win_rate | 0.4310 |
| sharpe_ratio | -5.3183 |
| sortino_ratio | -1.8870 |
| max_drawdown | 0.9019 |
| cagr | -0.5977 |
| net_avg_win | 39.6535 |
| net_avg_loss | -53.5070 |
| avg_hold_time_bars | 14.6207 |
| exposure | 0.4240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

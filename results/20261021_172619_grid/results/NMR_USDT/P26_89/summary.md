# EMA Hourly Continuation — NMR/USDT P26_89

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7933 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0395 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -2.0007 |
| sortino_ratio | -0.6667 |
| max_drawdown | 0.6138 |
| cagr | -0.2638 |
| net_avg_win | 75.4402 |
| net_avg_loss | -96.8661 |
| avg_hold_time_bars | 12.9464 |
| exposure | 0.3184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

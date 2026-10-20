# EMA Hourly Continuation — LPT/USDT P26_144

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.4271 |
| sortino_ratio | -1.1262 |
| max_drawdown | 0.7429 |
| cagr | -0.4117 |
| net_avg_win | 48.5638 |
| net_avg_loss | -67.2888 |
| avg_hold_time_bars | 17.9872 |
| exposure | 0.4456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

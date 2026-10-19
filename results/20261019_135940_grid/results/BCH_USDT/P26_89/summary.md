# EMA Hourly Continuation — BCH/USDT P26_89

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8801 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -5.7970 |
| sortino_ratio | -2.1642 |
| max_drawdown | 0.9295 |
| cagr | -0.6471 |
| net_avg_win | 31.1157 |
| net_avg_loss | -51.0501 |
| avg_hold_time_bars | 9.9540 |
| exposure | 0.3145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

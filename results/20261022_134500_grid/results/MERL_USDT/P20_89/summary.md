# EMA Hourly Continuation — MERL/USDT P20_89

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7028 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -3.3498 |
| sortino_ratio | -1.2353 |
| max_drawdown | 0.8012 |
| cagr | -0.4417 |
| net_avg_win | 56.7199 |
| net_avg_loss | -71.7421 |
| avg_hold_time_bars | 13.1529 |
| exposure | 0.4077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

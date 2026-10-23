# EMA Hourly Continuation — POPCAT/USDT P21_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5112 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.7134 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -5.7255 |
| sortino_ratio | -2.1710 |
| max_drawdown | 0.8979 |
| cagr | -0.6514 |
| net_avg_win | 35.4191 |
| net_avg_loss | -50.0277 |
| avg_hold_time_bars | 11.4604 |
| exposure | 0.3826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

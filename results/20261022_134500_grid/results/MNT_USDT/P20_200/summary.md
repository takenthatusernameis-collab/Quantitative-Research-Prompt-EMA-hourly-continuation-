# EMA Hourly Continuation — MNT/USDT P20_200

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6627 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.0340 |
| sortino_ratio | -0.5105 |
| max_drawdown | 0.5073 |
| cagr | -0.2171 |
| net_avg_win | 57.8165 |
| net_avg_loss | -84.0181 |
| avg_hold_time_bars | 47.2421 |
| exposure | 0.6829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

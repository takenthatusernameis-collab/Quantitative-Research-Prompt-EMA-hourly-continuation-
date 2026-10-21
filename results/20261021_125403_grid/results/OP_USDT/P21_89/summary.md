# EMA Hourly Continuation — OP/USDT P21_89

**Symbol:** OP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7363 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9149 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.0698 |
| sortino_ratio | -0.6253 |
| max_drawdown | 0.5350 |
| cagr | -0.2500 |
| net_avg_win | 66.8176 |
| net_avg_loss | -83.0251 |
| avg_hold_time_bars | 18.2756 |
| exposure | 0.3738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

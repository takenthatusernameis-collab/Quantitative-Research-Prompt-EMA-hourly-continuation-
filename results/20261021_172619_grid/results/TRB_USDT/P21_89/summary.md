# EMA Hourly Continuation — TRB/USDT P21_89

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6055 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.7602 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -3.5123 |
| sortino_ratio | -1.0521 |
| max_drawdown | 0.7152 |
| cagr | -0.3842 |
| net_avg_win | 56.1058 |
| net_avg_loss | -69.5900 |
| avg_hold_time_bars | 18.7133 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

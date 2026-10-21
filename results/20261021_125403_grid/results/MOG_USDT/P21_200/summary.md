# EMA Hourly Continuation — MOG/USDT P21_200

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -1.5917 |
| sortino_ratio | -0.3909 |
| max_drawdown | 0.3960 |
| cagr | -0.1655 |
| net_avg_win | 80.9188 |
| net_avg_loss | -93.5842 |
| avg_hold_time_bars | 45.8327 |
| exposure | 0.6266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

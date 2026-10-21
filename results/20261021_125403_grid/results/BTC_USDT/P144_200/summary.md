# EMA Hourly Continuation — BTC/USDT P144_200

**Symbol:** BTC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.7726 |
| net_win_rate | 0.5969 |
| gross_profit_factor | 1.4744 |
| gross_win_rate | 0.5969 |
| sharpe_ratio | -0.9936 |
| sortino_ratio | -0.1885 |
| max_drawdown | 0.2971 |
| cagr | -0.0819 |
| net_avg_win | 64.4886 |
| net_avg_loss | -123.5734 |
| avg_hold_time_bars | 7.3246 |
| exposure | 0.0560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZEC/USDT P20_200

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.4924 |
| sortino_ratio | -0.3948 |
| max_drawdown | 0.4193 |
| cagr | -0.1705 |
| net_avg_win | 66.9950 |
| net_avg_loss | -88.3983 |
| avg_hold_time_bars | 40.1029 |
| exposure | 0.6380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

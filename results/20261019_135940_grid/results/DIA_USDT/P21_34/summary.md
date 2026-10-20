# EMA Hourly Continuation — DIA/USDT P21_34

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.3053 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7471 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -9.5502 |
| sortino_ratio | -4.4295 |
| max_drawdown | 0.9965 |
| cagr | -0.8916 |
| net_avg_win | 9.3949 |
| net_avg_loss | -23.4718 |
| avg_hold_time_bars | 3.1532 |
| exposure | 0.1537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — KSM/USDT P34_89

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7446 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9961 |
| sortino_ratio | -0.6055 |
| max_drawdown | 0.5376 |
| cagr | -0.2418 |
| net_avg_win | 65.1964 |
| net_avg_loss | -87.5626 |
| avg_hold_time_bars | 10.9509 |
| exposure | 0.2230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

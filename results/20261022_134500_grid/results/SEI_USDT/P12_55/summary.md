# EMA Hourly Continuation — SEI/USDT P12_55

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -5.5402 |
| sortino_ratio | -2.4638 |
| max_drawdown | 0.9528 |
| cagr | -0.6964 |
| net_avg_win | 33.3148 |
| net_avg_loss | -47.2971 |
| avg_hold_time_bars | 8.2800 |
| exposure | 0.3790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

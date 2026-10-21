# EMA Hourly Continuation — XLM/USDT P26_89

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7755 |
| net_win_rate | 0.5230 |
| gross_profit_factor | 1.0902 |
| gross_win_rate | 0.5230 |
| sharpe_ratio | -1.5755 |
| sortino_ratio | -0.4857 |
| max_drawdown | 0.4603 |
| cagr | -0.1994 |
| net_avg_win | 61.8451 |
| net_avg_loss | -87.4345 |
| avg_hold_time_bars | 14.8162 |
| exposure | 0.3078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

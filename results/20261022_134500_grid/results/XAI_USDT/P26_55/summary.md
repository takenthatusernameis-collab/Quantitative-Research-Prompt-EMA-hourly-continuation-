# EMA Hourly Continuation — XAI/USDT P26_55

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.6005 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9771 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -6.2637 |
| sortino_ratio | -2.7255 |
| max_drawdown | 0.9668 |
| cagr | -0.7354 |
| net_avg_win | 32.5042 |
| net_avg_loss | -46.6064 |
| avg_hold_time_bars | 4.9710 |
| exposure | 0.2178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

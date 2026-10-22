# EMA Hourly Continuation — XAI/USDT P20_89

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7689 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.3072 |
| sortino_ratio | -0.7556 |
| max_drawdown | 0.6583 |
| cagr | -0.2942 |
| net_avg_win | 77.3080 |
| net_avg_loss | -90.7746 |
| avg_hold_time_bars | 17.7599 |
| exposure | 0.4270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

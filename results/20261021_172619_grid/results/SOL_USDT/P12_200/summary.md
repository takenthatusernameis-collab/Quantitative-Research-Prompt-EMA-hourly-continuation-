# EMA Hourly Continuation — SOL/USDT P12_200

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 1.0821 |
| net_win_rate | 0.5633 |
| gross_profit_factor | 1.2786 |
| gross_win_rate | 0.5633 |
| sharpe_ratio | 0.4241 |
| sortino_ratio | 0.0968 |
| max_drawdown | 0.1236 |
| cagr | 0.0377 |
| net_avg_win | 92.9440 |
| net_avg_loss | -110.7781 |
| avg_hold_time_bars | 69.2735 |
| exposure | 0.7715 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

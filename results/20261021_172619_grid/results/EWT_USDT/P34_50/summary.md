# EMA Hourly Continuation — EWT/USDT P34_50

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8352 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -2.3638 |
| sortino_ratio | -0.4935 |
| max_drawdown | 0.4329 |
| cagr | -0.2022 |
| net_avg_win | 68.5825 |
| net_avg_loss | -93.0673 |
| avg_hold_time_bars | 7.6233 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

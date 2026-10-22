# EMA Hourly Continuation — SLP/USDT P144_200

**Symbol:** SLP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.5863 |
| sortino_ratio | -0.3501 |
| max_drawdown | 0.3546 |
| cagr | -0.1476 |
| net_avg_win | 66.5425 |
| net_avg_loss | -95.9153 |
| avg_hold_time_bars | 6.2966 |
| exposure | 0.0675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

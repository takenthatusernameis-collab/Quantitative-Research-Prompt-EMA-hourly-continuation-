# EMA Hourly Continuation — AZERO/USDT P34_200

**Symbol:** AZERO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7726 |
| net_win_rate | 0.5160 |
| gross_profit_factor | 1.0675 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -1.2483 |
| sortino_ratio | -0.2912 |
| max_drawdown | 0.3694 |
| cagr | -0.1337 |
| net_avg_win | 71.1547 |
| net_avg_loss | -98.1984 |
| avg_hold_time_bars | 45.3879 |
| exposure | 0.5771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

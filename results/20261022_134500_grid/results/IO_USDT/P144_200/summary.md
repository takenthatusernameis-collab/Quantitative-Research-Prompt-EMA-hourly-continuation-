# EMA Hourly Continuation — IO/USDT P144_200

**Symbol:** IO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.5448 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8892 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -4.4187 |
| sortino_ratio | -1.3245 |
| max_drawdown | 0.7876 |
| cagr | -0.4799 |
| net_avg_win | 47.9953 |
| net_avg_loss | -74.1058 |
| avg_hold_time_bars | 4.1002 |
| exposure | 0.0852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

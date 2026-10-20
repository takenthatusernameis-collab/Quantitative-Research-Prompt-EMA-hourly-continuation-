# EMA Hourly Continuation — ZIL/USDT P12_55

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -6.8867 |
| sortino_ratio | -3.0001 |
| max_drawdown | 0.9760 |
| cagr | -0.7683 |
| net_avg_win | 22.0619 |
| net_avg_loss | -36.4814 |
| avg_hold_time_bars | 9.2183 |
| exposure | 0.4031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

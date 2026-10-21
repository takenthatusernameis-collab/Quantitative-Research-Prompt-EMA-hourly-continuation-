# EMA Hourly Continuation — JTO/USDT P12_20

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7974 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0952 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.5085 |
| sortino_ratio | -0.4312 |
| max_drawdown | 0.4375 |
| cagr | -0.1794 |
| net_avg_win | 75.4991 |
| net_avg_loss | -101.6639 |
| avg_hold_time_bars | 4.7132 |
| exposure | 0.0844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

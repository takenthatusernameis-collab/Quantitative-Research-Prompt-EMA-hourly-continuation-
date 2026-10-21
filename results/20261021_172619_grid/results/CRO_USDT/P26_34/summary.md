# EMA Hourly Continuation — CRO/USDT P26_34

**Symbol:** CRO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.5192 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.6697 |
| sortino_ratio | -0.5233 |
| max_drawdown | 0.4696 |
| cagr | -0.2155 |
| net_avg_win | 56.6510 |
| net_avg_loss | -95.8917 |
| avg_hold_time_bars | 4.9839 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

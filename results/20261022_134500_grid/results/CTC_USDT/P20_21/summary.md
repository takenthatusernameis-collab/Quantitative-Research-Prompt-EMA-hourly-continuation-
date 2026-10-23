# EMA Hourly Continuation — CTC/USDT P20_21

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1212 |
| net_profit_factor | 0.1064 |
| net_win_rate | 0.2962 |
| gross_profit_factor | 0.6620 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -17.8103 |
| sortino_ratio | -9.4922 |
| max_drawdown | 1.0000 |
| cagr | -0.9952 |
| net_avg_win | 3.3168 |
| net_avg_loss | -13.1193 |
| avg_hold_time_bars | 2.1304 |
| exposure | 0.1174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — OP/USDT P34_50

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.4026 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -8.0064 |
| sortino_ratio | -3.4744 |
| max_drawdown | 0.9876 |
| cagr | -0.8223 |
| net_avg_win | 15.4707 |
| net_avg_loss | -32.7165 |
| avg_hold_time_bars | 2.5914 |
| exposure | 0.1101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

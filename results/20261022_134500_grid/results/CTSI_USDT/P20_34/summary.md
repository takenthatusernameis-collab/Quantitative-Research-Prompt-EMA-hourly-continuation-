# EMA Hourly Continuation — CTSI/USDT P20_34

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1134 |
| net_profit_factor | 0.3879 |
| net_win_rate | 0.4162 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -10.1012 |
| sortino_ratio | -4.8348 |
| max_drawdown | 0.9977 |
| cagr | -0.9088 |
| net_avg_win | 13.3933 |
| net_avg_loss | -24.6181 |
| avg_hold_time_bars | 3.5397 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

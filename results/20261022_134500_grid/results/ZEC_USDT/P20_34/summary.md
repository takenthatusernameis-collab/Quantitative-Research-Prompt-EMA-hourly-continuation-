# EMA Hourly Continuation — ZEC/USDT P20_34

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.2710 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.7301 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -9.3434 |
| sortino_ratio | -4.2941 |
| max_drawdown | 0.9962 |
| cagr | -0.8906 |
| net_avg_win | 8.0139 |
| net_avg_loss | -22.5103 |
| avg_hold_time_bars | 2.6408 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

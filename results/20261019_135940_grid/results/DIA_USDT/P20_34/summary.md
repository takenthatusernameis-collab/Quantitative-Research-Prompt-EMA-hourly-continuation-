# EMA Hourly Continuation — DIA/USDT P20_34

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1095 |
| net_profit_factor | 0.3240 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.7507 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -9.4077 |
| sortino_ratio | -4.3913 |
| max_drawdown | 0.9962 |
| cagr | -0.8887 |
| net_avg_win | 10.0724 |
| net_avg_loss | -23.7278 |
| avg_hold_time_bars | 3.2603 |
| exposure | 0.1615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

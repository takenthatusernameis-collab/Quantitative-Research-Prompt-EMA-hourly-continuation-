# EMA Hourly Continuation — KAS/USDT P100_200

**Symbol:** KAS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.7688 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -4.7637 |
| sortino_ratio | -1.4102 |
| max_drawdown | 0.8331 |
| cagr | -0.5006 |
| net_avg_win | 31.7026 |
| net_avg_loss | -58.6918 |
| avg_hold_time_bars | 7.8243 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

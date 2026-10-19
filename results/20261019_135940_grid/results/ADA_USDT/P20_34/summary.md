# EMA Hourly Continuation — ADA/USDT P20_34

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.3405 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.9661 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -10.9084 |
| sortino_ratio | -5.2359 |
| max_drawdown | 0.9989 |
| cagr | -0.9326 |
| net_avg_win | 10.6110 |
| net_avg_loss | -23.1583 |
| avg_hold_time_bars | 2.5991 |
| exposure | 0.1347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — SOL/USDT P55_100

**Symbol:** SOL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.4313 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -6.7606 |
| sortino_ratio | -2.3492 |
| max_drawdown | 0.9512 |
| cagr | -0.6976 |
| net_avg_win | 26.7925 |
| net_avg_loss | -48.8623 |
| avg_hold_time_bars | 4.7430 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RPL/USDT P55_100

**Symbol:** RPL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.5645 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8818 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -4.1263 |
| sortino_ratio | -1.3910 |
| max_drawdown | 0.8086 |
| cagr | -0.4788 |
| net_avg_win | 39.3103 |
| net_avg_loss | -61.5405 |
| avg_hold_time_bars | 7.6543 |
| exposure | 0.1964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

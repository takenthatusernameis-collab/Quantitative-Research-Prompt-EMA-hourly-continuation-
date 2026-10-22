# EMA Hourly Continuation — RPL/USDT P34_55

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6362 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -3.3626 |
| sortino_ratio | -1.0575 |
| max_drawdown | 0.7088 |
| cagr | -0.3831 |
| net_avg_win | 54.2651 |
| net_avg_loss | -74.4669 |
| avg_hold_time_bars | 6.3429 |
| exposure | 0.1398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

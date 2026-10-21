# EMA Hourly Continuation — ARB/USDT P34_100

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.9040 |
| net_win_rate | 0.5364 |
| gross_profit_factor | 1.1470 |
| gross_win_rate | 0.5364 |
| sharpe_ratio | -0.5829 |
| sortino_ratio | -0.1711 |
| max_drawdown | 0.3010 |
| cagr | -0.0796 |
| net_avg_win | 80.1479 |
| net_avg_loss | -102.5803 |
| avg_hold_time_bars | 15.1650 |
| exposure | 0.2840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

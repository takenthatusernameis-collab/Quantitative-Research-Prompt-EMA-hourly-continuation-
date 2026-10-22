# EMA Hourly Continuation — TRX/USDT P12_20

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1255 |
| net_profit_factor | 0.0638 |
| net_win_rate | 0.2112 |
| gross_profit_factor | 0.8399 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -21.9589 |
| sortino_ratio | -13.2638 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 2.5709 |
| net_avg_loss | -10.7892 |
| avg_hold_time_bars | 2.5960 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

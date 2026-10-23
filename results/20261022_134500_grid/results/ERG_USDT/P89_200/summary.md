# EMA Hourly Continuation — ERG/USDT P89_200

**Symbol:** ERG/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.4203 |
| net_win_rate | 0.3800 |
| gross_profit_factor | 0.6393 |
| gross_win_rate | 0.3867 |
| sharpe_ratio | -5.8082 |
| sortino_ratio | -1.7502 |
| max_drawdown | 0.8782 |
| cagr | -0.5666 |
| net_avg_win | 37.1991 |
| net_avg_loss | -54.2518 |
| avg_hold_time_bars | 8.9178 |
| exposure | 0.1824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

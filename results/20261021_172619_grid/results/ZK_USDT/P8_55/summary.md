# EMA Hourly Continuation — ZK/USDT P8_55

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0253 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.5891 |
| sortino_ratio | -0.6150 |
| max_drawdown | 0.5355 |
| cagr | -0.2486 |
| net_avg_win | 74.2076 |
| net_avg_loss | -90.0059 |
| avg_hold_time_bars | 13.3926 |
| exposure | 0.4440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

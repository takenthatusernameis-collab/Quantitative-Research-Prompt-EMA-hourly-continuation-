# EMA Hourly Continuation — RAY/USDT P20_89

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.8285 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.3053 |
| sortino_ratio | -0.4073 |
| max_drawdown | 0.4520 |
| cagr | -0.1727 |
| net_avg_win | 76.8939 |
| net_avg_loss | -93.2053 |
| avg_hold_time_bars | 16.1621 |
| exposure | 0.3490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

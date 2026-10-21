# EMA Hourly Continuation — ZRX/USDT P8_12

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6286 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.4175 |
| sortino_ratio | -1.0902 |
| max_drawdown | 0.7176 |
| cagr | -0.3924 |
| net_avg_win | 49.3044 |
| net_avg_loss | -78.4407 |
| avg_hold_time_bars | 4.7102 |
| exposure | 0.1049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

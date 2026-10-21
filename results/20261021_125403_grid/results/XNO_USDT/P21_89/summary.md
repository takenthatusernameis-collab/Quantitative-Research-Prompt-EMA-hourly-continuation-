# EMA Hourly Continuation — XNO/USDT P21_89

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.6654 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -3.2424 |
| sortino_ratio | -1.0633 |
| max_drawdown | 0.7205 |
| cagr | -0.3872 |
| net_avg_win | 58.8899 |
| net_avg_loss | -71.6985 |
| avg_hold_time_bars | 13.0356 |
| exposure | 0.3164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

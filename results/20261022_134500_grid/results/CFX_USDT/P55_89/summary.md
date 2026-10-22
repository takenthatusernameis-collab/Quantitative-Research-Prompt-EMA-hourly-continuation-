# EMA Hourly Continuation — CFX/USDT P55_89

**Symbol:** CFX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.4559 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.7899 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -6.3295 |
| sortino_ratio | -2.2956 |
| max_drawdown | 0.9415 |
| cagr | -0.6749 |
| net_avg_win | 27.2728 |
| net_avg_loss | -46.7213 |
| avg_hold_time_bars | 4.3460 |
| exposure | 0.1302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

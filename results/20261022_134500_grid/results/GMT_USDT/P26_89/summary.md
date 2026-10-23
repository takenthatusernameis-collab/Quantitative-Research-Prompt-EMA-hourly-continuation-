# EMA Hourly Continuation — GMT/USDT P26_89

**Symbol:** GMT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.5301 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.8515 |
| gross_win_rate | 0.4362 |
| sharpe_ratio | -6.2610 |
| sortino_ratio | -2.4129 |
| max_drawdown | 0.9506 |
| cagr | -0.6897 |
| net_avg_win | 33.3816 |
| net_avg_loss | -46.6498 |
| avg_hold_time_bars | 8.7141 |
| exposure | 0.2979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

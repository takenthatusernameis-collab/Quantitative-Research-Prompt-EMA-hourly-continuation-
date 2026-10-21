# EMA Hourly Continuation — WOO/USDT P89_100

**Symbol:** WOO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 135 |
| net_profit_factor | 0.4941 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.7504 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -2.5186 |
| sortino_ratio | -0.4191 |
| max_drawdown | 0.3949 |
| cagr | -0.1754 |
| net_avg_win | 64.6362 |
| net_avg_loss | -98.5410 |
| avg_hold_time_bars | 4.1259 |
| exposure | 0.0253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ADA/USDT P8_21

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7941 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1196 |
| gross_win_rate | 0.5355 |
| sharpe_ratio | -1.3414 |
| sortino_ratio | -0.4186 |
| max_drawdown | 0.4604 |
| cagr | -0.1751 |
| net_avg_win | 59.3931 |
| net_avg_loss | -86.2169 |
| avg_hold_time_bars | 5.0946 |
| exposure | 0.1077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

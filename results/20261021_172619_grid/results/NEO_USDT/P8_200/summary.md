# EMA Hourly Continuation — NEO/USDT P8_200

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.9194 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1213 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.3829 |
| sortino_ratio | -0.0907 |
| max_drawdown | 0.2770 |
| cagr | -0.0439 |
| net_avg_win | 85.1024 |
| net_avg_loss | -104.2257 |
| avg_hold_time_bars | 66.7630 |
| exposure | 0.8194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

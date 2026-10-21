# EMA Hourly Continuation — MOG/USDT P55_100

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6712 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -2.2021 |
| sortino_ratio | -0.5745 |
| max_drawdown | 0.4600 |
| cagr | -0.2320 |
| net_avg_win | 65.3563 |
| net_avg_loss | -83.2906 |
| avg_hold_time_bars | 7.3182 |
| exposure | 0.1121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

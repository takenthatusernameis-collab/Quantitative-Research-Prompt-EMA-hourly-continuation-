# EMA Hourly Continuation — W/USDT P21_55

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.8227 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0305 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.5032 |
| sortino_ratio | -0.4931 |
| max_drawdown | 0.4802 |
| cagr | -0.2042 |
| net_avg_win | 76.7322 |
| net_avg_loss | -95.0684 |
| avg_hold_time_bars | 8.1836 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

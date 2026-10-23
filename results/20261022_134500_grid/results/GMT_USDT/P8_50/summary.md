# EMA Hourly Continuation — GMT/USDT P8_50

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1110 |
| net_profit_factor | 0.4828 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8276 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -7.2318 |
| sortino_ratio | -3.3674 |
| max_drawdown | 0.9855 |
| cagr | -0.8091 |
| net_avg_win | 18.5996 |
| net_avg_loss | -30.8960 |
| avg_hold_time_bars | 9.2117 |
| exposure | 0.4648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

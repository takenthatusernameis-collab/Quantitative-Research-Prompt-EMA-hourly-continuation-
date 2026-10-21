# EMA Hourly Continuation — GMT/USDT P8_34

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6730 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -3.1227 |
| sortino_ratio | -1.1850 |
| max_drawdown | 0.7548 |
| cagr | -0.4190 |
| net_avg_win | 45.5952 |
| net_avg_loss | -61.5209 |
| avg_hold_time_bars | 9.0283 |
| exposure | 0.2897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

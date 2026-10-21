# EMA Hourly Continuation — MOG/USDT P20_26

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.7225 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -1.4397 |
| sortino_ratio | -0.2765 |
| max_drawdown | 0.3028 |
| cagr | -0.1197 |
| net_avg_win | 83.6709 |
| net_avg_loss | -105.1526 |
| avg_hold_time_bars | 6.1084 |
| exposure | 0.0504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

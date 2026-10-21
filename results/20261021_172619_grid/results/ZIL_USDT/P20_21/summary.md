# EMA Hourly Continuation — ZIL/USDT P20_21

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.3520 |
| sortino_ratio | -0.2371 |
| max_drawdown | 0.2897 |
| cagr | -0.1027 |
| net_avg_win | 75.7111 |
| net_avg_loss | -112.9929 |
| avg_hold_time_bars | 4.9865 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

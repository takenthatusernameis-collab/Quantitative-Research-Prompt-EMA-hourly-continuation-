# EMA Hourly Continuation — ZEN/USDT P34_50

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.3304 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.7566 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -9.8215 |
| sortino_ratio | -4.4008 |
| max_drawdown | 0.9964 |
| cagr | -0.8935 |
| net_avg_win | 12.0192 |
| net_avg_loss | -25.0501 |
| avg_hold_time_bars | 2.6162 |
| exposure | 0.1193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

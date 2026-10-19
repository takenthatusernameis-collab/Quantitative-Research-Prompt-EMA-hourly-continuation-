# EMA Hourly Continuation — JST/USDT P20_21

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.0278 |
| net_win_rate | 0.2127 |
| gross_profit_factor | 0.4868 |
| gross_win_rate | 0.3952 |
| sharpe_ratio | -19.4909 |
| sortino_ratio | -10.5171 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 1.3563 |
| net_avg_loss | -13.1705 |
| avg_hold_time_bars | 2.1452 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

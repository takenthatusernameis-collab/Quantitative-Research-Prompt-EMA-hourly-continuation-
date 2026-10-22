# EMA Hourly Continuation — BCH/USDT P21_26

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.1383 |
| net_win_rate | 0.2968 |
| gross_profit_factor | 0.6210 |
| gross_win_rate | 0.3796 |
| sharpe_ratio | -17.3661 |
| sortino_ratio | -8.9849 |
| max_drawdown | 1.0000 |
| cagr | -0.9930 |
| net_avg_win | 4.6648 |
| net_avg_loss | -14.2389 |
| avg_hold_time_bars | 1.9051 |
| exposure | 0.1004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

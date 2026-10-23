# EMA Hourly Continuation — DIA/USDT P21_26

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1126 |
| net_profit_factor | 0.2029 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.7082 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -12.4285 |
| sortino_ratio | -5.9719 |
| max_drawdown | 0.9996 |
| cagr | -0.9563 |
| net_avg_win | 5.7711 |
| net_avg_loss | -18.3085 |
| avg_hold_time_bars | 2.2682 |
| exposure | 0.1156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

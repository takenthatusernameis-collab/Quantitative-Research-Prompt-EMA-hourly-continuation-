# EMA Hourly Continuation — AVA/USDT P20_26

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.2193 |
| net_win_rate | 0.3607 |
| gross_profit_factor | 0.7446 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -14.2534 |
| sortino_ratio | -7.0858 |
| max_drawdown | 0.9999 |
| cagr | -0.9770 |
| net_avg_win | 6.7206 |
| net_avg_loss | -17.2853 |
| avg_hold_time_bars | 2.0198 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

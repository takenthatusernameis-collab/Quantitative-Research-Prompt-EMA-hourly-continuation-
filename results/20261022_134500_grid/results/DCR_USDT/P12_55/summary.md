# EMA Hourly Continuation — DCR/USDT P12_55

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.4953 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.7985 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -7.1837 |
| sortino_ratio | -3.3482 |
| max_drawdown | 0.9839 |
| cagr | -0.8013 |
| net_avg_win | 20.1004 |
| net_avg_loss | -31.5696 |
| avg_hold_time_bars | 7.5880 |
| exposure | 0.3767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

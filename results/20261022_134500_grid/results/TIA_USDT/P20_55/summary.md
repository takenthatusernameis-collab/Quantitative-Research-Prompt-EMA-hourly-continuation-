# EMA Hourly Continuation — TIA/USDT P20_55

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -4.1708 |
| sortino_ratio | -1.7952 |
| max_drawdown | 0.8865 |
| cagr | -0.5735 |
| net_avg_win | 36.1076 |
| net_avg_loss | -54.4601 |
| avg_hold_time_bars | 5.6731 |
| exposure | 0.2390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

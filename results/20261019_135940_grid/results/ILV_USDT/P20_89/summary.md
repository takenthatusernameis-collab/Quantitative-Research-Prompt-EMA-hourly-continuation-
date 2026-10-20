# EMA Hourly Continuation — ILV/USDT P20_89

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6780 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -3.7043 |
| sortino_ratio | -1.4266 |
| max_drawdown | 0.8175 |
| cagr | -0.4866 |
| net_avg_win | 47.3890 |
| net_avg_loss | -67.2876 |
| avg_hold_time_bars | 11.1916 |
| exposure | 0.3744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

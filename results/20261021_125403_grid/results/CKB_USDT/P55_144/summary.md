# EMA Hourly Continuation — CKB/USDT P55_144

**Symbol:** CKB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7746 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5313 |
| sortino_ratio | -0.4138 |
| max_drawdown | 0.4027 |
| cagr | -0.1740 |
| net_avg_win | 73.6110 |
| net_avg_loss | -95.0265 |
| avg_hold_time_bars | 13.8876 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

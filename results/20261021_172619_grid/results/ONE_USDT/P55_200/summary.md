# EMA Hourly Continuation — ONE/USDT P55_200

**Symbol:** ONE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.8456 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0078 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9009 |
| sortino_ratio | -0.2167 |
| max_drawdown | 0.2839 |
| cagr | -0.0966 |
| net_avg_win | 87.4331 |
| net_avg_loss | -103.4011 |
| avg_hold_time_bars | 26.4149 |
| exposure | 0.3386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

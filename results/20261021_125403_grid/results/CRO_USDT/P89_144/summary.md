# EMA Hourly Continuation — CRO/USDT P89_144

**Symbol:** CRO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -2.2948 |
| sortino_ratio | -0.5425 |
| max_drawdown | 0.4921 |
| cagr | -0.2195 |
| net_avg_win | 60.1529 |
| net_avg_loss | -91.5416 |
| avg_hold_time_bars | 8.2472 |
| exposure | 0.1016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

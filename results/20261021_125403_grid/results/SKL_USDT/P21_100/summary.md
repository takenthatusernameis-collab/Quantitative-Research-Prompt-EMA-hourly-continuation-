# EMA Hourly Continuation — SKL/USDT P21_100

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7811 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -1.7209 |
| sortino_ratio | -0.5184 |
| max_drawdown | 0.5160 |
| cagr | -0.2127 |
| net_avg_win | 74.2682 |
| net_avg_loss | -90.4901 |
| avg_hold_time_bars | 20.9011 |
| exposure | 0.4228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

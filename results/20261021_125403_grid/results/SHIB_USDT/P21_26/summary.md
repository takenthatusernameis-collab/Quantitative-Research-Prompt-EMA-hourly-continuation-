# EMA Hourly Continuation — SHIB/USDT P21_26

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 129 |
| net_profit_factor | 0.6761 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9891 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.4188 |
| sortino_ratio | -0.2318 |
| max_drawdown | 0.2864 |
| cagr | -0.1010 |
| net_avg_win | 76.5184 |
| net_avg_loss | -111.4321 |
| avg_hold_time_bars | 4.2171 |
| exposure | 0.0247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

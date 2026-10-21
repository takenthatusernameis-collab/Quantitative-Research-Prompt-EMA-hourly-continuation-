# EMA Hourly Continuation — ONE/USDT P55_100

**Symbol:** ONE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8603 |
| net_win_rate | 0.5257 |
| gross_profit_factor | 1.1135 |
| gross_win_rate | 0.5257 |
| sharpe_ratio | -0.8702 |
| sortino_ratio | -0.2286 |
| max_drawdown | 0.3077 |
| cagr | -0.1010 |
| net_avg_win | 83.0585 |
| net_avg_loss | -106.9941 |
| avg_hold_time_bars | 8.1208 |
| exposure | 0.1222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

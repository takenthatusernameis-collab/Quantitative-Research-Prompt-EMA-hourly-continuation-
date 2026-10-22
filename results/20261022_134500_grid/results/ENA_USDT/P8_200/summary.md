# EMA Hourly Continuation — ENA/USDT P8_200

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8332 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.9162 |
| sortino_ratio | -0.2278 |
| max_drawdown | 0.2800 |
| cagr | -0.1036 |
| net_avg_win | 76.4038 |
| net_avg_loss | -95.9770 |
| avg_hold_time_bars | 58.8306 |
| exposure | 0.8210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

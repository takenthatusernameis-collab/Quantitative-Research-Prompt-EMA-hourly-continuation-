# EMA Hourly Continuation — ENJ/USDT P12_34

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1271 |
| net_profit_factor | 0.4247 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.8479 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -8.9960 |
| sortino_ratio | -4.5218 |
| max_drawdown | 0.9965 |
| cagr | -0.8930 |
| net_avg_win | 12.9503 |
| net_avg_loss | -24.6375 |
| avg_hold_time_bars | 4.1227 |
| exposure | 0.2371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ACE/USDT P34_200

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.9024 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0728 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -0.5088 |
| sortino_ratio | -0.1261 |
| max_drawdown | 0.2517 |
| cagr | -0.0596 |
| net_avg_win | 85.6218 |
| net_avg_loss | -102.1329 |
| avg_hold_time_bars | 37.9365 |
| exposure | 0.5133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

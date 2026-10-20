# EMA Hourly Continuation — OGN/USDT P55_200

**Symbol:** OGN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.8035 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -3.8679 |
| sortino_ratio | -1.1195 |
| max_drawdown | 0.7550 |
| cagr | -0.4110 |
| net_avg_win | 42.1929 |
| net_avg_loss | -64.9313 |
| avg_hold_time_bars | 20.4123 |
| exposure | 0.3898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

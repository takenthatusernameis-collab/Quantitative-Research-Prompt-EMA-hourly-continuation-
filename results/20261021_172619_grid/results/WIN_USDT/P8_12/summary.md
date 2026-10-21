# EMA Hourly Continuation — WIN/USDT P8_12

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.5421 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.8392 |
| sortino_ratio | -0.6019 |
| max_drawdown | 0.5090 |
| cagr | -0.2417 |
| net_avg_win | 58.7027 |
| net_avg_loss | -95.1126 |
| avg_hold_time_bars | 5.8889 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

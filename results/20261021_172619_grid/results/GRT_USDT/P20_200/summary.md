# EMA Hourly Continuation — GRT/USDT P20_200

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 1.1087 |
| net_win_rate | 0.5636 |
| gross_profit_factor | 1.2693 |
| gross_win_rate | 0.5636 |
| sharpe_ratio | 0.5211 |
| sortino_ratio | 0.1123 |
| max_drawdown | 0.1181 |
| cagr | 0.0452 |
| net_avg_win | 96.9972 |
| net_avg_loss | -113.0033 |
| avg_hold_time_bars | 72.0091 |
| exposure | 0.7169 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

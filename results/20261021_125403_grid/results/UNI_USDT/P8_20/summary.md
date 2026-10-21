# EMA Hourly Continuation — UNI/USDT P8_20

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7651 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0517 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.7953 |
| sortino_ratio | -0.5457 |
| max_drawdown | 0.5247 |
| cagr | -0.2208 |
| net_avg_win | 66.5038 |
| net_avg_loss | -90.9072 |
| avg_hold_time_bars | 5.2040 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LTC/USDT P21_144

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.3898 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.7555 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -5.6667 |
| sortino_ratio | -1.8199 |
| max_drawdown | 0.8992 |
| cagr | -0.5901 |
| net_avg_win | 25.8279 |
| net_avg_loss | -48.4873 |
| avg_hold_time_bars | 21.2715 |
| exposure | 0.5057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

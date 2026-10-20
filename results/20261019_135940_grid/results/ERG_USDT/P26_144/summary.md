# EMA Hourly Continuation — ERG/USDT P26_144

**Symbol:** ERG/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4281 |
| net_win_rate | 0.4051 |
| gross_profit_factor | 0.6352 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -5.8947 |
| sortino_ratio | -2.0218 |
| max_drawdown | 0.9142 |
| cagr | -0.6203 |
| net_avg_win | 28.5705 |
| net_avg_loss | -45.4406 |
| avg_hold_time_bars | 14.7220 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

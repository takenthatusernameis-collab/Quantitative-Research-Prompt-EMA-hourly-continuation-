# EMA Hourly Continuation — ENS/USDT P26_34

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1138 |
| net_profit_factor | 0.3164 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.7480 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -13.2087 |
| sortino_ratio | -6.4234 |
| max_drawdown | 0.9998 |
| cagr | -0.9676 |
| net_avg_win | 10.7860 |
| net_avg_loss | -20.6282 |
| avg_hold_time_bars | 2.1520 |
| exposure | 0.1113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

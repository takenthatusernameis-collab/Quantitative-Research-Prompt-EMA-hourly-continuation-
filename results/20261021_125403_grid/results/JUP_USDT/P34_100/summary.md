# EMA Hourly Continuation — JUP/USDT P34_100

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.0596 |
| sortino_ratio | -0.3060 |
| max_drawdown | 0.3748 |
| cagr | -0.1334 |
| net_avg_win | 72.1173 |
| net_avg_loss | -90.1934 |
| avg_hold_time_bars | 12.6305 |
| exposure | 0.2331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MOG/USDT P12_26

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7306 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.6102 |
| sortino_ratio | -0.8156 |
| max_drawdown | 0.6203 |
| cagr | -0.3135 |
| net_avg_win | 76.5334 |
| net_avg_loss | -90.9880 |
| avg_hold_time_bars | 6.0839 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

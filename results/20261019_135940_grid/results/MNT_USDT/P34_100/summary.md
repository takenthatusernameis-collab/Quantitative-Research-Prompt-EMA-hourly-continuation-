# EMA Hourly Continuation — MNT/USDT P34_100

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.3814 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.7282 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -6.4834 |
| sortino_ratio | -2.2331 |
| max_drawdown | 0.9452 |
| cagr | -0.6751 |
| net_avg_win | 22.8283 |
| net_avg_loss | -43.8164 |
| avg_hold_time_bars | 9.6938 |
| exposure | 0.2648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

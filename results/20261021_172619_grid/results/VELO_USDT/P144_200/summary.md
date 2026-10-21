# EMA Hourly Continuation — VELO/USDT P144_200

**Symbol:** VELO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.7408 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.3177 |
| sortino_ratio | -0.2734 |
| max_drawdown | 0.2778 |
| cagr | -0.1182 |
| net_avg_win | 75.9035 |
| net_avg_loss | -95.8805 |
| avg_hold_time_bars | 6.2512 |
| exposure | 0.0600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

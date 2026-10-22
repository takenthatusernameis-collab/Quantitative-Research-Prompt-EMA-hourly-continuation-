# EMA Hourly Continuation — CTSI/USDT P8_200

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.9052 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0830 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.4797 |
| sortino_ratio | -0.1198 |
| max_drawdown | 0.1680 |
| cagr | -0.0566 |
| net_avg_win | 82.7855 |
| net_avg_loss | -99.7153 |
| avg_hold_time_bars | 57.9767 |
| exposure | 0.7932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

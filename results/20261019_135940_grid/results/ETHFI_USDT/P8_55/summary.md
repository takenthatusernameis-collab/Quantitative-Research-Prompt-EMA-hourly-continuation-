# EMA Hourly Continuation — ETHFI/USDT P8_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.6074 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8920 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -5.1133 |
| sortino_ratio | -2.3015 |
| max_drawdown | 0.9359 |
| cagr | -0.6632 |
| net_avg_win | 30.7061 |
| net_avg_loss | -43.3740 |
| avg_hold_time_bars | 10.6637 |
| exposure | 0.4944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

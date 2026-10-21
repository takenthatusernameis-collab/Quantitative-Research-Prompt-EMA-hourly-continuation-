# EMA Hourly Continuation — EUL/USDT P21_200

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8260 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9649 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -0.9714 |
| sortino_ratio | -0.2443 |
| max_drawdown | 0.2735 |
| cagr | -0.1079 |
| net_avg_win | 77.3553 |
| net_avg_loss | -91.2680 |
| avg_hold_time_bars | 39.0194 |
| exposure | 0.5498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

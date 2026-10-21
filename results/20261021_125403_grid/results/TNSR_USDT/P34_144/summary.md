# EMA Hourly Continuation — TNSR/USDT P34_144

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7718 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -1.6465 |
| sortino_ratio | -0.4618 |
| max_drawdown | 0.4360 |
| cagr | -0.1923 |
| net_avg_win | 75.3183 |
| net_avg_loss | -90.3456 |
| avg_hold_time_bars | 22.4165 |
| exposure | 0.3946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

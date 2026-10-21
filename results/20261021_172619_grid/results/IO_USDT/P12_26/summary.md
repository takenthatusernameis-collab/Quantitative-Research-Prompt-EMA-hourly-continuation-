# EMA Hourly Continuation — IO/USDT P12_26

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -2.0055 |
| sortino_ratio | -0.6122 |
| max_drawdown | 0.5337 |
| cagr | -0.2450 |
| net_avg_win | 70.5862 |
| net_avg_loss | -88.7587 |
| avg_hold_time_bars | 5.1051 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

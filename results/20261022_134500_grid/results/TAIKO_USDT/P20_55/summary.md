# EMA Hourly Continuation — TAIKO/USDT P20_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.5434 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -6.3965 |
| sortino_ratio | -2.6864 |
| max_drawdown | 0.9621 |
| cagr | -0.7359 |
| net_avg_win | 28.7865 |
| net_avg_loss | -46.3064 |
| avg_hold_time_bars | 6.1166 |
| exposure | 0.2494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

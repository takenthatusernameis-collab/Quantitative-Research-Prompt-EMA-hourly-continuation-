# EMA Hourly Continuation — RENDER/USDT P34_200

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.8778 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -0.6189 |
| sortino_ratio | -0.1458 |
| max_drawdown | 0.2072 |
| cagr | -0.0673 |
| net_avg_win | 84.4914 |
| net_avg_loss | -100.4701 |
| avg_hold_time_bars | 42.1245 |
| exposure | 0.5180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

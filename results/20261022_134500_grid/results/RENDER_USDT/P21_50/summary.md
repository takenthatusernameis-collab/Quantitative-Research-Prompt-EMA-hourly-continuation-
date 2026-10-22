# EMA Hourly Continuation — RENDER/USDT P21_50

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.5165 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -7.4113 |
| sortino_ratio | -3.3541 |
| max_drawdown | 0.9721 |
| cagr | -0.8036 |
| net_avg_win | 26.4421 |
| net_avg_loss | -40.7915 |
| avg_hold_time_bars | 4.0124 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

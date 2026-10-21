# EMA Hourly Continuation — PEPE/USDT P12_21

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0404 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.1314 |
| sortino_ratio | -0.2641 |
| max_drawdown | 0.2786 |
| cagr | -0.1143 |
| net_avg_win | 73.8645 |
| net_avg_loss | -98.4295 |
| avg_hold_time_bars | 4.3080 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ARB/USDT P8_144

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7259 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0549 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.8706 |
| sortino_ratio | -0.5138 |
| max_drawdown | 0.4643 |
| cagr | -0.2154 |
| net_avg_win | 63.9283 |
| net_avg_loss | -89.0078 |
| avg_hold_time_bars | 47.0452 |
| exposure | 0.8040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

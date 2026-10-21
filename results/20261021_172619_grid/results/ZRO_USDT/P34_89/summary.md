# EMA Hourly Continuation — ZRO/USDT P34_89

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.9722 |
| net_win_rate | 0.5433 |
| gross_profit_factor | 1.1753 |
| gross_win_rate | 0.5433 |
| sharpe_ratio | -0.1154 |
| sortino_ratio | -0.0354 |
| max_drawdown | 0.2300 |
| cagr | -0.0239 |
| net_avg_win | 85.0361 |
| net_avg_loss | -104.0409 |
| avg_hold_time_bars | 10.4159 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

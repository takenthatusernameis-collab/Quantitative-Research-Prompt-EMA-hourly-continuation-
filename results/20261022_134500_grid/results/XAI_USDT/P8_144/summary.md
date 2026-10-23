# EMA Hourly Continuation — XAI/USDT P8_144

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7794 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.9445 |
| sortino_ratio | -0.5647 |
| max_drawdown | 0.5954 |
| cagr | -0.2376 |
| net_avg_win | 82.7075 |
| net_avg_loss | -104.6330 |
| avg_hold_time_bars | 41.1482 |
| exposure | 0.7949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

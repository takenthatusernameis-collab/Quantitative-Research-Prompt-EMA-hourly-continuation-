# EMA Hourly Continuation — ZRX/USDT P20_34

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.3286 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.7313 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -11.0139 |
| sortino_ratio | -5.3190 |
| max_drawdown | 0.9988 |
| cagr | -0.9302 |
| net_avg_win | 10.5793 |
| net_avg_loss | -21.9074 |
| avg_hold_time_bars | 3.2287 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

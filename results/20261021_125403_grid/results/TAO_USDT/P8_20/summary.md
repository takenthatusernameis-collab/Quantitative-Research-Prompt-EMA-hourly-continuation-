# EMA Hourly Continuation — TAO/USDT P8_20

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.8735 |
| net_win_rate | 0.5319 |
| gross_profit_factor | 1.1244 |
| gross_win_rate | 0.5319 |
| sharpe_ratio | -0.8307 |
| sortino_ratio | -0.2468 |
| max_drawdown | 0.3823 |
| cagr | -0.1102 |
| net_avg_win | 78.0034 |
| net_avg_loss | -101.4727 |
| avg_hold_time_bars | 5.4350 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

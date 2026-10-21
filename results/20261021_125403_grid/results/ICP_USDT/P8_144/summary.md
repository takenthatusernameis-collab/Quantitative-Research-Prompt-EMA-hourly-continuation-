# EMA Hourly Continuation — ICP/USDT P8_144

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8106 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.1516 |
| sortino_ratio | -0.2989 |
| max_drawdown | 0.3162 |
| cagr | -0.1300 |
| net_avg_win | 77.4817 |
| net_avg_loss | -92.7402 |
| avg_hold_time_bars | 50.6707 |
| exposure | 0.7624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

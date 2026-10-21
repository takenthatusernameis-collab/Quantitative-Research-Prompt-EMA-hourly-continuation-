# EMA Hourly Continuation — LDO/USDT P50_144

**Symbol:** LDO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.3830 |
| sortino_ratio | -0.3600 |
| max_drawdown | 0.3674 |
| cagr | -0.1534 |
| net_avg_win | 78.1249 |
| net_avg_loss | -95.0064 |
| avg_hold_time_bars | 19.3724 |
| exposure | 0.2932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
